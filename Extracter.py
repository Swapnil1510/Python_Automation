from playwright.sync_api import sync_playwright

def test_excel_connection():
    print("🚀 Starting Playwright Test...")
    
    # 1. Start Playwright
    with sync_playwright() as p:
        
        # 2. Launch Browser (Persistent Context)
        # Yeh bohot important hai. Tera regular Chrome URL direct kholta hai kyunki usme tera session/cookie save hai.
        # Playwright by default naya, khali browser kholta hai. 
        # 'user_data_dir' use karne se Playwright tera login session save kar lega 'chrome_session' folder mein.
        browser = p.chromium.launch_persistent_context(
            user_data_dir="./chrome_session", # Is folder mein tera login save hoga
            headless=False,                   # False rakha hai taaki hum browser open hote hue dekh sakein
            channel="chrome",                 # Tere system ka actual Google Chrome use karega
            args=["--start-maximized"],       # Full screen mein open hoga
            no_viewport=True
        )
        
        page = browser.pages[0]
        
        # YAHAN TERA ACTUAL SHAREPOINT URL DAALNA HAI
        excel_url = "https://att.sharepoint.com/:x:/r/sites/Artemis_Program_Management/_layouts/15/doc2.aspx?..." 
        
        print(f"🌐 Navigating to URL: {excel_url[:50]}...")
        page.goto(excel_url)
        
        # 3. Wait for User / Grid to Load
        print("⏳ Waiting for Excel grid to load...")
        # Pehli baar run karne pe shayad Microsoft login maange, isliye main yahan 20 seconds ka wait daal raha hu.
        # Tu manually login kar lena agar pooche toh. Agli baar se nahi poochega.
        page.wait_for_timeout(20000) 
        
        # 4. Check if we reached the page
        title = page.title()
        print(f"✅ Success! Current Page Title is: {title}")
        
        # 5. Keep it open for 10 more seconds to observe, then close
        print("👀 Look at the browser... Closing in 10 seconds.")
        page.wait_for_timeout(10000)
        
        browser.close()
        print("🛑 Browser Closed.")

# Script run karne ke liye
if __name__ == "__main__":
    test_excel_connection()