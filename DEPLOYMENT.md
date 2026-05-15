# Deployment Guide: blaguesa2balles.party

## ✅ Phase 1: GitHub - COMPLETE
Repository: https://github.com/thomas-rabaux-dev/blaguesa2balles-party

---

## 📦 Phase 2: Deploy to Vercel

### Step 1: Sign up/Login to Vercel
1. Go to https://vercel.com
2. Click "Sign Up" (or "Login" if you have an account)
3. Choose "Continue with GitHub"
4. Authorize Vercel to access your GitHub account

### Step 2: Import Your Repository
1. Click "Add New..." → "Project"
2. Select "Import Git Repository"
3. Search for `blaguesa2balles-party`
4. Click "Import"

### Step 3: Configure & Deploy
1. **Framework Preset**: Select "Other" (it's a static site)
2. **Root Directory**: Leave as `.`
3. **Build Command**: Leave empty (no build needed)
4. **Output Directory**: Leave empty
5. Click **"Deploy"**

⏱️ Wait ~30 seconds for deployment to complete

✅ Your site will be live at: `https://blaguesa2balles-party.vercel.app`

---

## 🌐 Phase 3: Connect Custom Domain (blaguesa2balles.party)

### Step 1: Add Domain in Vercel
1. In your Vercel project dashboard, go to **Settings** → **Domains**
2. Enter: `blaguesa2balles.party`
3. Click "Add"
4. Vercel will show you DNS records to configure

### Step 2: Configure DNS in Cloudflare

#### Login to Cloudflare
1. Go to https://dash.cloudflare.com
2. Select your domain `blaguesa2balles.party`
3. Click on **DNS** → **Records**

#### Add DNS Records
Vercel will ask you to add either:

**Option A: A Record (Recommended)**
```
Type: A
Name: @
Content: 76.76.21.21
Proxy status: DNS only (gray cloud)
TTL: Auto
```

**Option B: CNAME Record**
```
Type: CNAME
Name: @
Content: cname.vercel-dns.com
Proxy status: DNS only (gray cloud)
TTL: Auto
```

**For www subdomain (optional):**
```
Type: CNAME
Name: www
Content: cname.vercel-dns.com
Proxy status: DNS only (gray cloud)
TTL: Auto
```

### Step 3: Wait for DNS Propagation
- Can take 5 minutes to 48 hours (usually ~10-30 minutes)
- Check status in Vercel dashboard
- Once verified, Vercel automatically provisions SSL certificate

### Step 4: Enable Cloudflare Proxy (Optional - After SSL is active)
Once Vercel shows SSL as active:
1. Go back to Cloudflare DNS settings
2. Toggle "Proxy status" to **Proxied** (orange cloud)
3. This enables Cloudflare's CDN and DDoS protection

---

## 🎯 Final Result

Your website will be accessible at:
- ✅ https://blaguesa2balles.party (main domain)
- ✅ https://www.blaguesa2balles.party (if you added www)
- ✅ https://blaguesa2balles-party.vercel.app (Vercel URL)

**Features:**
- ✅ Free hosting forever
- ✅ Automatic HTTPS/SSL
- ✅ Global CDN
- ✅ Auto-deploy on git push
- ✅ Cloudflare DDoS protection

---

## 🔄 Future Updates

To update your website:
```bash
cd /Users/thomas.rabaux/Documents/Personal/WebReconstruction
# Make your changes to HTML/images
git add .
git commit -m "Your update description"
git push
```

Vercel will automatically rebuild and deploy within ~30 seconds!

---

## 🆘 Troubleshooting

### Domain not working after 1 hour?
1. Check DNS propagation: https://dnschecker.org
2. Verify Cloudflare proxy is OFF (gray cloud) until SSL is active
3. Make sure DNS records exactly match what Vercel shows

### SSL certificate not provisioning?
- Wait up to 24 hours
- Ensure Cloudflare proxy is OFF initially
- Check that A record points to correct IP

### Need help?
- Vercel docs: https://vercel.com/docs/concepts/projects/domains
- Cloudflare docs: https://developers.cloudflare.com/dns/
