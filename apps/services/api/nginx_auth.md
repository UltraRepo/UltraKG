# 🔐 NGINX Proxy Manager – Basic Auth Setup Guide

This guide explains how to secure any UltraKG service (like the public landing page at `ai.yourdomain.com`) using **Basic Authentication** in **NGINX Proxy Manager**.

Use this to ensure that only users with credentials can access your landing page or internal services.

---

## ✅ Step 1: Log into NGINX Proxy Manager

Access the NPM UI at:

```
http://localhost:81
```

Use the admin account you set up during deployment.

---

## ✅ Step 2: Create a Basic Auth Access List

1. Go to the sidebar and click:  
   **Access Lists → Add Access List**

2. Fill out the form:
   - **Name**: `LoginRequired`
   - ✅ Enable **"Satisfy Any"**
   - ✅ Add a user:
     - **Username**: `testuser`
     - **Password**: `testpass`

3. Click **Save**

---

## ✅ Step 3: Apply Access List to Your Landing Page

1. Go to: **Hosts → Proxy Hosts**
2. Edit the host for your landing page (e.g., `ai.yourdomain.com`)
3. Navigate to the **Access List** tab
4. Enable:
   - ✅ **Access List**
   - Select: `LoginRequired`
5. Save

---

## 🔁 Result

Now when someone visits `https://ai.yourdomain.com`, they will see a **basic auth prompt**:

```
Username: testuser
Password: testpass
```

After entering valid credentials, they will be allowed to access the page (e.g., `index.html` served via FastAPI).

---

## 🧠 Why Use NGINX Auth?

- No need to add auth logic to your FastAPI code
- Centralized access control for all services
- Can manage credentials via GUI
- Compatible with any Docker-based service in the UltraKG stack

---

## 📌 Notes

- For stronger security in production, use long, random passwords.
- You can create multiple access lists for different groups or endpoints.
- Never expose unauthenticated endpoints to the public internet unless intended.

---

