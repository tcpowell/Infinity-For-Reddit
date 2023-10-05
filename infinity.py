import os

username = input("Enter username: ")
apiKey = input("Enter API key: ")
version = input("Enter Version: ")

buildFile = "app/build.gradle"
apiFile = "app/src/main/java/ml/docilealligator/infinityforreddit/utils/APIUtils.java"
stringFile = "app/src/main/res/values/strings.xml"

with open(buildFile, "r") as input_file, open(buildFile+".tp", "w") as output_file:
    for line in input_file:
        if "versionName " in line and version == "TBD":
            version = line.replace('"', '').replace("versionName", "").strip()
            output_file.write(line)
        elif "buildTypes {" in line:
            output_file.write('    signingConfigs {' + "\n")
            output_file.write('        release {' + "\n")
            output_file.write('            storeFile file("/content/Infinity.jks")' + "\n")
            output_file.write('            storePassword "Infinity"' + "\n")
            output_file.write('            keyAlias "Infinity"' + "\n")
            output_file.write('            keyPassword "Infinity"' + "\n")
            output_file.write('        }' + "\n")
            output_file.write('    }' + "\n\n")
            output_file.write('    buildTypes {' + "\n")
            output_file.write('        release {' + "\n")
            output_file.write('            signingConfig signingConfigs.release' + "\n")
        elif "release {" in line:
            continue
        else:
            output_file.write(line)

with open(apiFile, "r") as input_file, open(apiFile+".tp", "w") as output_file:
    for line in input_file:
        if "public static final String CLIENT_ID = " in line:
            output_file.write('    public static final String CLIENT_ID = "'+apiKey+'";' + "\n")
        elif "public static final String REDIRECT_URI = " in line:
            output_file.write('    public static final String REDIRECT_URI = "http://127.0.0.1";' + "\n");
        elif "public static final String USER_AGENT = " in line:
            output_file.write('    public static final String USER_AGENT = "android:personal-app:v'+version+' (by /u/'+username+')";' + "\n");
        else:
            output_file.write(line)

with open(stringFile, "r", encoding="utf8") as input_file, open(stringFile+".tp", "w", encoding="utf8") as output_file:
    for line in input_file:
        if '<string name="application_name"' in line:
            output_file.write(line.replace("Infinity", "Reddit (Infinity)"))
        else:
            output_file.write(line)

os.replace(buildFile+".tp", buildFile)
os.replace(apiFile+".tp", apiFile)
os.replace(stringFile+".tp", stringFile)
