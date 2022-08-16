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
- [x] Sign up Workflow
- [x] Two auth Workflow
- [X] Reset Password Workflow
- [x] Redirect user to the right page
- [x] Change header if user logged or not
- [x] Get user infos from backend
- [x] My profile page basic infos
- [X] Edit infos user
- [ ] My profile page box's scheduled infos
- [ ] CRUD box schedule
- [ ] Create Flash messages html
- [ ] Tests Frontend
- [ ] Deploy
