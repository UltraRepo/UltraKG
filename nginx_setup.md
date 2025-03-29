# 🌐 UltraKG - NGINX Proxy Manager Setup Guide

This guide walks you through configuring NGINX Proxy Manager (NPM) to route and secure traffic to your UltraKG FastAPI landing page (`index.html`), including basic HTTP authentication.

---

### 🧭 How to Add a Proxy Host in NGINX Proxy Manager

1. Open your browser and visit:  
   `http://localhost:81` (the default admin panel for NGINX Proxy Manager)

2. Log in using your admin credentials

3. Navigate to:  
   **Dashboard → Hosts → Proxy Hosts**

4. Click **"Add Proxy Host"**

5. Fill in the details:

| Field | Value |
|-------|-------|
| **Domain Names** | e.g., `ai.ultrakg.com` |
| **Scheme** | `http` |
| **Forward Hostname / IP** | Docker service name, e.g., `fastapi` |
| **Forward Port** | `8000` (or whichever port FastAPI uses) |
| **Websockets Support** | ✅ Enabled |
| **Block Common Exploits** | ✅ Enabled |

6. Switch to the **SSL tab**:

| Setting | Action |
|---------|--------|
| **SSL Certificate** | Select **“Request a new SSL Certificate”** |
| **Force SSL** | ✅ Enabled |
| **HTTP/2 Support** | ✅ Enabled |

7. Click **Save**

Once complete, traffic to `https://ai.ultrakg.com` will be routed to your internal FastAPI app and optionally secured with authentication.

---

## 🔐 NGINX Basic Auth for Landing Page

To restrict access to the public `index.html` landing page (served via FastAPI), use **NGINX Proxy Manager’s Access List** feature for simple HTTP Basic Auth.

🧩 This prevents unauthorized users from even seeing the page — ideal for dev, staging, or internal admin portals.

> 📄 Fast NGINX Auth setup for admins:  
> [Nginx_Auth](nginx_auth.md)

---

### ✅ Step-by-Step: Add Basic Auth

1. Log into **NGINX Proxy Manager** at `http://localhost:81`
2. Go to **Access Lists → Add Access List**
3. Create a list:
   - **Name**: `LoginRequired`
   - ✅ Check **"Satisfy Any"**
   - ✅ Add a user:
     - **Username**: `testuser`
     - **Password**: `testpass` (you’ll enter this in plaintext; it will be hashed automatically)
4. Click **Save**

---

### 🔐 Apply Access List to a Proxy Host

1. Go back to **Hosts → Proxy Hosts**
2. Edit the proxy host for `ai.ultrakg.com`
3. Go to the **Access List** tab:
   - ✅ Enable **Access List**
   - Select **`LoginRequired`** from the dropdown
4. Save your changes

---

### 🎯 Result

Now, when a user visits `https://ai.ultrakg.com`, they will first be prompted with a browser login dialog:

- **Username**: `testuser`  
- **Password**: `testpass`

If the credentials are correct, they’ll be granted access to the `index.html` landing page served by your FastAPI backend.

> This approach ensures simple, centralized authentication without needing to modify your FastAPI app logic.

---

### ✅ Final Step

To verify:

- Log out and log back in via an incognito/private window
- Navigate to `https://ai.ultrakg.com`
- Enter your test credentials
- You should see the default UltraKG landing page (`index.html`)
