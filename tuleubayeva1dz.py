#This is a project with a WAV file 505-Arctic Monkeys. Result: 22679901 number of numbers < 16000, 1664172 number of numbers > 16000

def wavNum(lst, n):
   ls_count = 0 #the number of elements is less than n
   gt_count = 0 #the number of elements is greater than n
   for i in lst:
      if abs(i) < n:
         ls_count += 1
      if abs(i) > n:
         gt_count += 1
   return (ls_count, gt_count)

def decode(file_path):
   data = None
   result = []
   with open(file_path, mode="rb") as file:
      data = file.read()[44:] #without heading

   for start, end in zip(range(0, len(data)-2, 2), range(2, len(data), 2)):
      val = int.from_bytes(data[start:end], byteorder="little", signed=True) #transmit a list of bytes, byte order, signature
      result.append(val)

   return result

if __name__ == "__main__":
   data = decode("./file.wav")
   #print(data, len(data), min(data), max(data)) #just for control
   print(wavNum(data, 16000))