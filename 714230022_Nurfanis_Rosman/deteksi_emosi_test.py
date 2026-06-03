import os
import time
import unittest
# pyrefly: ignore [missing-import]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MoodieEmotionDetectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Konfigurasi Chrome Options
        chrome_options = Options()
        # Menggunakan headless mode agar dapat berjalan dengan lancar di server/background
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Inisialisasi WebDriver
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.base_url = "https://moodie-dusky.vercel.app/"
        print("\n=== Memulai Pengujian Selenium WebDriver untuk Aplikasi Moodie ===")
        print(f"Target URL: {cls.base_url}\n")

    @classmethod
    def tearDownClass(cls):
        # Menutup WebDriver setelah seluruh pengujian selesai
        cls.driver.quit()
        print("\n=== Seluruh Pengujian Selesai & WebDriver Ditutup ===")

    def setUp(self):
        # Membuka halaman web sebelum setiap test case
        self.driver.get(self.base_url)
        # Menunggu sampai dropdown emosi tersedia di halaman
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.ID, "emotionDropdown")))

    def test_01_page_title_and_layout(self):
        """1. Verifikasi Judul Halaman dan Elemen Default Halaman Utama"""
        print("[TEST 01] Memverifikasi judul halaman dan tata letak default...")
        
        # Verifikasi judul halaman
        self.assertEqual(self.driver.title, "Moodie - Deteksi Emosi", "Judul halaman tidak sesuai!")
        
        # Verifikasi header
        header_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(header_text, "Moodie", "Header aplikasi tidak sesuai!")

        # Verifikasi elemen default di tab deteksi
        emotion_text = self.driver.find_element(By.ID, "selectedEmotion").text
        self.assertEqual(emotion_text, "Pilihan: -", "Default teks pilihan emosi salah!")

        emotion_icon = self.driver.find_element(By.ID, "emotionIcon").text
        self.assertEqual(emotion_icon, "🙂", "Default emoji salah!")

        motivasi_text = self.driver.find_element(By.ID, "motivasi").text
        self.assertEqual(motivasi_text, "", "Default motivasi seharusnya kosong!")

        tips_text = self.driver.find_element(By.ID, "tips").text
        self.assertEqual(tips_text, "", "Default tips seharusnya kosong!")
        print("-> [PASSED] Judul halaman dan status default valid.")

    def test_02_deteksi_senang(self):
        """2. Deteksi Emosi: Senang"""
        print("[TEST 02] Menguji deteksi emosi 'Senang'...")
        
        # Pilih emosi Senang dari dropdown
        dropdown = Select(self.driver.find_element(By.ID, "emotionDropdown"))
        dropdown.select_by_value("Senang")

        # Klik tombol deteksi
        button_deteksi = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Deteksi Emosi')]")
        button_deteksi.click()

        # Verifikasi hasil
        time.sleep(1) # Tunggu perubahan render singkat
        selected_text = self.driver.find_element(By.ID, "selectedEmotion").text
        self.assertEqual(selected_text, "Pilihan: Senang", "Teks pilihan tidak terupdate menjadi Senang!")

        emoji = self.driver.find_element(By.ID, "emotionIcon").text
        self.assertEqual(emoji, "😊", "Emoji tidak berubah menjadi 😊!")

        motivasi = self.driver.find_element(By.ID, "motivasi").text
        self.assertEqual(motivasi, "Nikmati setiap momen bahagia hari ini! 🌞", "Motivasi senang tidak cocok!")

        tips = self.driver.find_element(By.ID, "tips").text
        self.assertEqual(tips, "Bagikan kebahagiaanmu dengan orang lain atau lakukan hal yang kamu sukai. 🎉", "Tips senang tidak cocok!")
        print("-> [PASSED] Deteksi emosi 'Senang' berhasil diverifikasi.")

    def test_03_deteksi_sedih(self):
        """3. Deteksi Emosi: Sedih"""
        print("[TEST 03] Menguji deteksi emosi 'Sedih'...")
        
        # Pilih emosi Sedih dari dropdown
        dropdown = Select(self.driver.find_element(By.ID, "emotionDropdown"))
        dropdown.select_by_value("Sedih")

        # Klik tombol deteksi
        button_deteksi = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Deteksi Emosi')]")
        button_deteksi.click()

        # Verifikasi hasil
        time.sleep(1)
        selected_text = self.driver.find_element(By.ID, "selectedEmotion").text
        self.assertEqual(selected_text, "Pilihan: Sedih", "Teks pilihan tidak terupdate menjadi Sedih!")

        emoji = self.driver.find_element(By.ID, "emotionIcon").text
        self.assertEqual(emoji, "😢", "Emoji tidak berubah menjadi 😢!")

        motivasi = self.driver.find_element(By.ID, "motivasi").text
        self.assertEqual(motivasi, "Tidak apa-apa merasa sedih. 💙", "Motivasi sedih tidak cocok!")

        tips = self.driver.find_element(By.ID, "tips").text
        self.assertEqual(tips, "Luangkan waktu untuk berbicara dengan orang terdekat atau menulis perasaanmu. 📓", "Tips sedih tidak cocok!")
        print("-> [PASSED] Deteksi emosi 'Sedih' berhasil diverifikasi.")

    def test_04_deteksi_marah(self):
        """4. Deteksi Emosi: Marah"""
        print("[TEST 04] Menguji deteksi emosi 'Marah'...")
        
        # Pilih emosi Marah dari dropdown
        dropdown = Select(self.driver.find_element(By.ID, "emotionDropdown"))
        dropdown.select_by_value("Marah")

        # Klik tombol deteksi
        button_deteksi = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Deteksi Emosi')]")
        button_deteksi.click()

        # Verifikasi hasil
        time.sleep(1)
        selected_text = self.driver.find_element(By.ID, "selectedEmotion").text
        self.assertEqual(selected_text, "Pilihan: Marah", "Teks pilihan tidak terupdate menjadi Marah!")

        emoji = self.driver.find_element(By.ID, "emotionIcon").text
        self.assertEqual(emoji, "😠", "Emoji tidak berubah menjadi 😠!")

        motivasi = self.driver.find_element(By.ID, "motivasi").text
        self.assertEqual(motivasi, "Kamu berhak marah, tapi jangan biarkan amarah menguasai hatimu. 🔥", "Motivasi marah tidak cocok!")

        tips = self.driver.find_element(By.ID, "tips").text
        self.assertEqual(tips, "Cobalah menarik napas dalam-dalam dan menghembuskannya perlahan. 🧘‍♂️", "Tips marah tidak cocok!")
        print("-> [PASSED] Deteksi emosi 'Marah' berhasil diverifikasi.")

    def test_05_deteksi_netral(self):
        """5. Deteksi Emosi: Netral"""
        print("[TEST 05] Menguji deteksi emosi 'Netral'...")
        
        # Pilih emosi Netral dari dropdown
        dropdown = Select(self.driver.find_element(By.ID, "emotionDropdown"))
        dropdown.select_by_value("Netral")

        # Klik tombol deteksi
        button_deteksi = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Deteksi Emosi')]")
        button_deteksi.click()

        # Verifikasi hasil
        time.sleep(1)
        selected_text = self.driver.find_element(By.ID, "selectedEmotion").text
        self.assertEqual(selected_text, "Pilihan: Netral", "Teks pilihan tidak terupdate menjadi Netral!")

        emoji = self.driver.find_element(By.ID, "emotionIcon").text
        self.assertEqual(emoji, "😐", "Emoji tidak berubah menjadi 😐!")

        motivasi = self.driver.find_element(By.ID, "motivasi").text
        self.assertEqual(motivasi, "Hari yang tenang kadang justru paling berarti. 🌿", "Motivasi netral tidak cocok!")

        tips = self.driver.find_element(By.ID, "tips").text
        self.assertEqual(tips, "Gunakan waktu ini untuk refleksi diri atau menikmati kesunyian. ☕", "Tips netral tidak cocok!")
        print("-> [PASSED] Deteksi emosi 'Netral' berhasil diverifikasi.")

    def test_06_navigation(self):
        """6. Pengujian Navigasi Antar Tab"""
        print("[TEST 06] Menguji sistem navigasi tab...")

        # Bagian awal (deteksi) harus terlihat, grafik dan panduan tersembunyi secara default
        deteksi_section = self.driver.find_element(By.ID, "deteksi")
        grafik_section = self.driver.find_element(By.ID, "grafik")
        panduan_section = self.driver.find_element(By.ID, "panduan")

        self.assertTrue("active" in deteksi_section.get_attribute("class"), "Tab deteksi harusnya aktif secara default")
        self.assertFalse("active" in grafik_section.get_attribute("class"), "Tab grafik harusnya tidak aktif secara default")
        self.assertFalse("active" in panduan_section.get_attribute("class"), "Tab panduan harusnya tidak aktif secara default")

        # Klik tab Grafik Riwayat Emosi
        tab_grafik = self.driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Grafik Riwayat Emosi')]")
        tab_grafik.click()
        time.sleep(1)

        self.assertFalse("active" in deteksi_section.get_attribute("class"), "Tab deteksi harusnya tidak aktif")
        self.assertTrue("active" in grafik_section.get_attribute("class"), "Tab grafik harusnya aktif sekarang")

        # Klik tab Panduan Penggunaan
        tab_panduan = self.driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Panduan Penggunaan')]")
        tab_panduan.click()
        time.sleep(1)

        self.assertFalse("active" in grafik_section.get_attribute("class"), "Tab grafik harusnya tidak aktif")
        self.assertTrue("active" in panduan_section.get_attribute("class"), "Tab panduan harusnya aktif sekarang")

        # Klik tab Deteksi Emosi untuk kembali ke semula
        tab_deteksi = self.driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Deteksi Emosi')]")
        tab_deteksi.click()
        time.sleep(1)

        self.assertTrue("active" in deteksi_section.get_attribute("class"), "Tab deteksi harusnya aktif kembali")
        self.assertFalse("active" in panduan_section.get_attribute("class"), "Tab panduan harusnya tidak aktif")
        print("-> [PASSED] Navigasi tab berfungsi dengan baik dan mengubah class 'active'.")

    def test_07_heatmap_update(self):
        """7. Pengujian Pembaruan Heatmap Saat Deteksi Sukses"""
        print("[TEST 07] Menguji pembaruan dinamis pada Heatmap Emosi...")

        # Hitung jumlah heat-block saat ini di heatmap container sebelum deteksi
        heatmap_container = self.driver.find_element(By.ID, "heatmapContainer")
        blocks_before = len(heatmap_container.find_elements(By.CLASS_NAME, "heat-block"))

        # Pilih emosi Senang dari dropdown
        dropdown = Select(self.driver.find_element(By.ID, "emotionDropdown"))
        dropdown.select_by_value("Senang")

        # Klik tombol deteksi
        button_deteksi = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Deteksi Emosi')]")
        button_deteksi.click()
        time.sleep(1)

        # Hitung jumlah heat-block setelah deteksi
        blocks_after = len(heatmap_container.find_elements(By.CLASS_NAME, "heat-block"))

        # Jumlah blok harus bertambah 1
        self.assertEqual(blocks_after, blocks_before + 1, "Jumlah heat-block di heatmap tidak bertambah!")

        # Pastikan blok baru memiliki kelas emosi yang sesuai
        last_block = heatmap_container.find_elements(By.CLASS_NAME, "heat-block")[-1]
        self.assertTrue("senang" in last_block.get_attribute("class").lower(), "Blok baru di heatmap tidak memiliki class 'senang'!")
        print(f"-> [PASSED] Jumlah heatmap block bertambah dari {blocks_before} menjadi {blocks_after} dengan class 'senang'.")

    def test_08_download_chart(self):
        """8. Pengujian Klik Tombol Unduh Grafik"""
        print("[TEST 08] Menguji interaksi tombol Unduh Grafik...")

        # Pindah ke tab Grafik Riwayat Emosi agar tombol terlihat/dapat diklik
        tab_grafik = self.driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Grafik Riwayat Emosi')]")
        tab_grafik.click()
        time.sleep(1)

        # Temukan tombol unduh grafik
        button_download = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Unduh Grafik Emosi')]")
        
        # Verifikasi tombol aktif dan dapat diklik
        self.assertTrue(button_download.is_displayed(), "Tombol unduh grafik tidak ditampilkan di tab Grafik!")
        self.assertTrue(button_download.is_enabled(), "Tombol unduh grafik dinonaktifkan!")
        
        # Klik tombol unduh
        button_download.click()
        time.sleep(1)
        print("-> [PASSED] Tombol Unduh Grafik berhasil diklik tanpa error.")

if __name__ == "__main__":
    unittest.main()
