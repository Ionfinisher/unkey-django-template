# Django endpoint protection with Unkey RBAC

---

## Overview

This a starter Django application which implements API key verification with Unkey RBAC. There are two endpoints, a public one and a protected one that requires a valid API Key.

## Features

- Public endpoint accessible without authenticationn
- Protected endpoint only accessible with a valid API key
- Verification service to check API key validity on protected route

## Quickstart

---

## Create a permission and role

1. Go to app/authorization/permissions and click on the "Create New Permission" button.
2. Enter call-protected-route as the name and add a description if you want.
3. Click "Create New Permission"
4. Now head over to /app/authorization/roles and click on the "Create New Role" button.
5. Enter a name for the role, for example, admin and select the permission from the prevous step
6. Click "Create".

## Create your API

1. Go to https://app.unkey.com/apis and click on the "Create New API" button.
2. Give it a name.
3. Click "Create".

## Create your first key

1. Click "Create Key" in the top right corner.
2. Click "Create"
3. Copy the key and save it somewhere safe.

## Connect the key to the role

1. Go to /app/apis and click on the API you created.
2. Click on "Keys" in the tabs.
3. Click on the key you created.
4. Click on "Permissions" in the tabs.
5. Check the role's checkbox to give the key the role and permission.

## Set up the example

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <folder-root>
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Change the .env.example to .env file and add the following:

   ```bash
   UNKEY_ROOT_KEY=your-root-key
   UNKEY_API_ID=your-api-id
   ```

5. Start the server

   ```bash
   cd src/django-unkey/template_api
   python manage.py runserver
   ```

6. curl the unprotected route

   ```bash
    curl http://127.0.0.1:8000/api/v1/public
   ```

   It should return Heeyaaa!! Touchdown to the public endpoint!!

7. curl the protected route

   ```bash
    curl http://127.0.0.1:8000/api/v1/protected -H "Authorization: Bearer <YOUR_KEY>"
   ```

   It should return Woohoo!! Touchdown to the protected endpoint!!

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact [your-email@example.com].
