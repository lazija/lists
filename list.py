import os
path = 'E:/3D_BODY/3d_model/hips_and_legs1to10'
files = os.listdir(path)
x="}},"
for f in files:
    with open('dodaj_text.txt','a+', encoding="utf-8") as text_file:
        text_file.write('{Filename: "%s", Class : "#b1f2ff", wikipediaInfos : { en: "Left_coronary_artery", sr: "Артерија"'%f+x+'\n')
print("Done, all is add in 'text.txt'")
