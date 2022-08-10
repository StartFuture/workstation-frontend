# workstation-backend

Back-End of Workstation Project

## Run file Linux

```python
pip install -r requirements.txt
cd app
gunicorn -w 2 -b 127.0.0.1:8000 app:app
```

## Todo

- [x] Connection Backend
- [x] Authentication with jwt
- [x] Login Workflow
- [ ] Sign up Workflow
- [x] Two auth Workflow
- [ ] Reset Password Workflow
- [x] Redirect user to the right page
- [x] Change header if user logged or not
- [x] Get user infos from backend
- [x] My profile page basic infos
- [ ] My profile page box's scheduled infos
- [ ] Edit infos user
- [ ] CRUD box schedule
