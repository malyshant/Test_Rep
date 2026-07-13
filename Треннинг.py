s = "Здравствуйте, Гости"
# res = s[1:12]
# res = s [11]
# res = s[1:12]
# res=s[::-1] # start:stop:step
# print (res)
s1 = "казак"
# if s1 == s1[::-1]:
#     print ("Palindrom")
# # else:
# #     print("No")
#     print (s.count("s"))
# s1 = " aaa bbb ccc ddd"
# s2 = " 111 222 333 444"
# res = ""
# res = s1[:4] + s2[:4]
# for i in range(0, len(s1), 4):
#     res += s1[i:i + 4] + s2[i:i + 4]
# print(res)
# s1 = 'aaa bbb ccc ddd eee'
# s2 = '111 222 333 444 555'
#
# res = ''
#
# for i in range(0, len(s1), 4):
#     res += s1[i:i + 4] + s2[i:i + 4]
# print(res)
s1 =input('Word: ')
res='Palindrom' if s1 == s1[::-1]   else None if s1[0]=='k' else "No"
print (res)
