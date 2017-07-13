all_data = """graph TD\n    Cloudant-->CoreService\n    Cloudant-->Platform\n
Cloudant-->Architecture\n    Cloudant-->ProgramManagement\n    subgraph\n
     CoreService-->Docs\n        CoreService-->DB\n CoreService-->SAPI\n
  CoreService-->Operations\n        Operations-->CN\n Operations-->UK\n
Operations-->US\n    end\n    Platform-->Infra\n    Platform-->InfraOps\n
 Platform-->Integrations\n    Platform-->Performance\n
Platform-->PrelEng\n    PrelEng-->Beacon\n    Platform-->Security\n
Architecture-->MikeRhodes\n    Architecture-->PaulDavis\n
DB-->BalakrishnaKolla\n    DB-->EricAvdey\n    DB-->IlyaK\n
DB-->JayDoane\n    DB-->MayyaSharipova\n    DB-->NicolaeVatamaniuc\n
DB-->PENGHUIJIANG\n    DB-->Russell\n    DB-->TonySun\n
Docs-->AdrianWarman\n    Docs-->LoraBoe\n    Infra-->ChunHuiWang\n
Infra-->CletoMartin\n    Infra-->EMREYILDIRIM\n    Infra-->MatthewWhite\n
 InfraOps-->PaulSzczypka\n    InfraOps-->RobAllen\n
InfraOps-->TREVORSEHRER\n    Integrations-->EstebanLaver\n
Integrations-->RichardEllis\n    Integrations-->SamSmith\n
Integrations-->TomBlench\n    US-->AaronDocherty\n    CN-->DanZhu\n
CN-->JingWang\n    US-->JohnHarrison\n    US-->MadhuGaur\n
UK-->MohammedTalukder\n    UK-->PaulNightingale\n    UK-->RobertNewson\n
US-->SeanConway\n    CN-->ShuQiZhong\n    UK-->Temitope\n CN-->YunZheng\n
 CN-->ZanZhou\n    ProgramManagement-->DavidBelsky\n
ProgramManagement-->DenitsaBurroughs\n    ProgramManagement-->EricaPegg\n
 ProgramManagement-->JezzKelway\n    ProgramManagement-->JozefdeVries\n
ProgramManagement-->KeerthiSukumaran\n ProgramManagement-->SimonMetson\n
PrelEng-->KyleSnavely\n    Beacon-->DanielCheeseman\n
Beacon-->JamesMackenzie\n    Beacon-->WenLi\n    SAPI-->EricAppelt\n
SAPI-->JordanCounts\n    SAPI-->RhysShort\n    SAPI-->SeanHudgston\n
Security-->Bradley\n    Security-->DonaldBryanGreen\n
Security-->GrahamThackrah\n    Security-->YaliWang"""
lists = all_data.split("\n")
list_split=[]
while "" in lists:
    lists.remove("")
for i in range (0,len(lists)):
    lists[i]=lists[i].strip()

for data in lists:
    if "-->" in data:
        list_split.append(data.split("-->"))

#print(list_split)
Cloudant  = {}
for cloudant in list_split:
    Cloudant[cloudant[0]] = []
print (Cloudant)
for people in list_split:
    Cloudant[people[0]].append(people[1])

print(Cloudant)
