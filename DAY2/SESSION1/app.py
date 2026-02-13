import streamlit as st

st.title("PassWord Validation and Encryption")

password=st.text_input("Enter the password",type="password")

if st.button("Validate and Encrypt"):
    if password=="":
        st.warning("Please Enter Password")
    elif len(password)<=8:
        st.error("Password must be atleast 8 char")
    elif password[4] not in "12345":
        st.error("The fifth char must be 1-5 range")
    elif not password.isalnum():
        st.error("Must contain alphabet and numeric")
    
    else:
        has_upper=any(i.isupper() for i in password)
        has_lower=any(i.islower() for i in password)

        if not (has_upper and has_lower):
            st.error("Must contain 1 Upper and 1 Lower")

        else:
            encrypted_password=password.replace("A","@").replace("a","B").replace("b","1")

            st.success("Thank you for Entering Valid Password\n")
            st.write("The Encrypted Password: ")
            st.code(encrypted_password)