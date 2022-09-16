resource "aws_s3_bucket" "default" {
  bucket = var.bucket_id

  tags = {
    Name = "${var.bucket_id}"
  }
}

resource "aws_s3_bucket_policy" "allow_access" {
  bucket = aws_s3_bucket.default.id
  policy = data.aws_iam_policy_document.allow_access.json
}

resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.default.id
}

resource "aws_s3_bucket_website_configuration" "web_config" {
  bucket = aws_s3_bucket.default.bucket

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

resource "aws_s3_object" "website_files" {
  for_each = fileset(var.upload_directory, "**/*.*")
  bucket   = aws_s3_bucket.default.bucket
  key      = replace(each.value, var.upload_directory, "")
  source   = "${var.upload_directory}${each.value}"
  acl      = "public-read"
  etag     = filemd5("${var.upload_directory}${each.value}")
  content_type  = lookup(var.mime_types, split(".", each.value)[length(split(".", each.value)) - 1])
}

