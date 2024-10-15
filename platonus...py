auditornuyi = float(input("орташа  бағасын енгізіңіз (0-ден 100-ге дейін): "))
Module1 = float(input("Модул 1(0-ден 100-ге дейін): "))
Module2= float(input("Модул 2 (0-ден 100-ге дейін): "))
session_baqasy = float(input("Сессиядан қанша аламын деп ойлайсыз (0-ден 100-ге дейін): "))




qorytyndy_baqa = (auditornuyi * 0.4 +Module1*0.1+Module2 *0.1+ session_baqasy * 0.4)


print("Сіздің қорытынды бағаңыз: ", qorytyndy_baqa)