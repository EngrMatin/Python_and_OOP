import subprocess
import sys


# proc = subprocess.Popen(["python", "-c", "import writer; writer.write()"], stdout=subprocess.PIPE)
# proc = subprocess.Popen(["python", "-c", "import writer; writer.write()"], capture_output=True)
# out = proc.communicate()[0]
# print(out.upper())

result = subprocess.run([sys.executable, "-c", "print('ocean')"], capture_output=True, text=True)

print("stdout:", result.stdout)
print("stderr:", result.stderr)


result2 = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True)

print("stdout:", result2.stdout)
print("stderr:", result2.stderr)