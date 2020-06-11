import pymysql

db = pymysql.connect("localhost", "root", "intel@123", "dlib_database")

cursor = db.cursor()

features_to_write = [-0.05093818406263987, 0.12188426529367764, 0.021663098596036434, 0.007112744419525067, 0.019947169348597527, -0.017684168182313442, -0.06240454067786535, -0.14904101441303888, 0.12912110487620035, -0.06539999321103096, 0.32668980459372204, -0.08956715961297353, -0.2233349730571111, -0.16316535075505575, -0.043568329885602, 0.15306122601032257, -0.22560513019561768, -0.05824261096616586, 0.0008928601940472921, 0.005215682089328766, 0.07045721262693405, -0.010809733998030424, 0.08229426294565201, 0.030403127272923786, -0.057094186544418335, -0.3901691436767578, -0.09786246592799823, -0.1366340791185697, 0.08081211894750595, -0.05840929597616196, -0.08377094566822052, 0.09646281475822131, -0.1572437286376953, -0.07211034744977951, 0.014857079523305098, 0.05128619633615017, -0.02317502722144127, 0.008807960043971738, 0.21670926610628763, 0.014430611239125332, -0.1106676956017812, 0.013356470813353857, -0.013254943924645582, 0.3010881543159485, 0.2180469756325086, 0.03937635198235512, 0.021555060675988596, -0.1261985289553801, 0.07927998527884483, -0.1812665412823359, -0.01797958432386319, 0.1701841006676356, 0.05328188960750898, 0.0638671734680732, -0.0071110886832078295, -0.07812172546982765, -0.002902708171556393, 0.016050405179460842, -0.12456538155674934, 0.04371590353548527, 0.06866196853419144, -0.09843112155795097, -0.07189957052469254, -0.039837307607134186, 0.22565458218256632, 0.03891558696826299, -0.11568417027592659, -0.158128559589386, 0.0989462211728096, -0.14065119375785193, -0.0791608989238739, 0.06185196712613106, -0.17062974721193314, -0.1588644360502561, -0.31957850356896716, 0.0028169795405119658, 0.37459876636664075, 0.056846046820282936, -0.19854066024223962, 0.07432499652107556, -0.061530095214645066, -0.042603561033805214, 0.16889012853304544, 0.15522447476784387, 0.0013788302118579547, 0.01416956369454662, -0.09725802764296532, 0.011324269231408834, 0.16411483784516653, -0.10624602437019348, -0.05069482823212942, 0.2191446622212728, -0.058212711165348686, 0.14107660204172134, 0.05972097317377726, 0.03836750239133835, -0.008183061766127745, 0.013461803396542868, -0.15975585083166757, -0.016289977356791496, 0.06424866430461407, -0.04501990042626858, -0.014299487229436636, 0.08307581146558125, -0.12795844053228697, 0.0907629740734895, 0.020792022347450256, 0.051313288509845734, 0.10030742858846982, -0.03910529613494873, -0.10968481873472531, -0.07072770098845164, 0.16106270253658295, -0.2536987190445264, 0.19503900657097498, 0.19389603535334268, 0.061460199455420174, 0.07509348417321841, 0.09566772232453029, 0.0804272231956323, -0.03687311274309953, 0.004403541640688975, -0.19420884301265082, -0.02305115247145295, 0.047012136628230415, 0.030078041056791942, -0.001907990003625552, -0.06858471284310023]
# cursor.execute("insert into dlib_face_table(, ")

person_cnt = 10

# insert person_1 to person_...
for i in range(person_cnt):
    print("insert into dlib_face_table(person_x) values(\"person_"+str(i+1)+"\");")
    # cursor.execute("insert into dlib_face_table(person_x) values(\"person_"+str(i+1)+"\");")


cursor.execute("desc dlib_face_table;")
# cursor.execute("insert into dlib_face_table(feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10, feature_11, feature_12, feature_13, feature_14, feature_15, feature_16, feature_17, feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, feature_26, feature_27, feature_28, feature_29, feature_30, feature_31, feature_32, feature_33, feature_34, feature_35, feature_36, feature_37, feature_38, feature_39, feature_40, feature_41, feature_42, feature_43, feature_44, feature_45, feature_46, feature_47, feature_48, feature_49, feature_50, feature_51, feature_52, feature_53, feature_54, feature_55, feature_56, feature_57, feature_58, feature_59, feature_60, feature_61, feature_62, feature_63, feature_64, feature_65, feature_66, feature_67, feature_68, feature_69, feature_70, feature_71, feature_72, feature_73, feature_74, feature_75, feature_76, feature_77, feature_78, feature_79, feature_80, feature_81, feature_82, feature_83, feature_84, feature_85, feature_86, feature_87, feature_88, feature_89, feature_90, feature_91, feature_92, feature_93, feature_94, feature_95, feature_96, feature_97, feature_98, feature_99, feature_100, feature_101, feature_102, feature_103, feature_104, feature_105, feature_106, feature_107, feature_108, feature_109, feature_110, feature_111, feature_112, feature_113, feature_114, feature_115, feature_116, feature_117, feature_118, feature_119, feature_120, feature_121, feature_122, feature_123, feature_124, feature_125, feature_126, feature_127, feature_128) values"
#                "\"")
#
for i in range(128):
    # update issue_info set github_status='Open', github_type='bug' where github_id='2222';
    print("update dlib_face_table set feature_"+str(i+1)+'=\"'+ str(features_to_write[i])+"\" where person_x=\"person_"+str(i+1)+"\";")

results = cursor.fetchall()

print(results)