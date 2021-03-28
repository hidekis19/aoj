import sys 
alps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
members = [] 
for i in sys.stdin.readlines(): 
    members.append(i.rstrip()) 

member=' '.join(members)

x = member.lower()
for alp in alps:
    alp_cnt = x.count(alp)
    print(alp + " : " + str(alp_cnt))