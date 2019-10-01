import requests

# 下载图片并返:回图片名称
def download_img(img_path, img_url):
    try:
        img_res = requests.get(img_url)
        if img_res.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(img_res.content)    
            return True
        return False
    except requests.RequestException:
        return False

def get_html(page_url, encoding = "utf-8"):
    try: 
        response = requests.get(page_url)
        response.encoding = encoding
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        print(page_url+'请求失败')
        return None


