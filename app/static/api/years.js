function generateArrayOfYears() {
  var max = new Date().getFullYear()
  var min = max - 60
  var years = []

  for (var i = max; i >= min; i--) {
    years.push(i)
  }
  return years
}
for (var i = min; i<=max; i++){
    var opt = document.createElement('option');
    opt.value = i;
    opt.innerHTML = i;
   document.getElementById('years').appendChild(opt)
}

var years = generateArrayOfYears().toString();
document.getElementById('years')