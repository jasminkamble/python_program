
msg="hello"

# Encode string to bytes
encode_msg= msg.encode("utf-8")
print(encode_msg)

# Decode bytes back to string
decode_msg=encode_msg.decode("utf-8")
print(decode_msg)