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
- [x] Change header if user loggedasd or not
- [x] Get user infos from backend
- [x] My profile page basic infos
- [X] Edit infos user
- [X] CRUD box
- [ ] Search Box
- [ ] CRUD schedule
- [ ] My profile page box's scheduled infos
- [ ] Create Flash messages html ? Optional
- [ ] Tests Frontend
- [ ] Deploy
