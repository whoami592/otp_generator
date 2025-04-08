import random

def generate_otp():
    # Generate a 6-digit OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return otp

def main():
    print("Simple OTP Generator by Mr. Sabaz Ali Khan")
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
    
    # Simulate OTP verification (for demonstration)
    user_input = input("Enter the OTP to verify: ")
    if user_input == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP!")

if __name__ == "__main__":
    main()