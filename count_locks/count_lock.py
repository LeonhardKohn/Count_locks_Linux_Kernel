import subprocess
import re

# Execute shell command
shell_command = "rg mutex_lock | wc -l"

# Get all branch tags
git_tag_command = ["git", "-C", "linux", "tag", "-l"]
git_tag_result = subprocess.run(git_tag_command, capture_output=True, text=True)
git_branch_tags = git_tag_result.stdout.strip().split("\n")
branch_tag_list = []
for tag in git_branch_tags:
    branch_tag_list.append(tag)
branch_tag_list.sort(key=lambda x: int(x.split(".")[1].split("-")[0]))
branch_tag_list.sort(key=lambda x: x.split(".")[0])
print(branch_tag_list)

# Open file for writing results
output_file = open("results_mutex_lock.txt", "w")

# Iterate through branch tags
for branch_tag in branch_tag_list:
    # Checkout branch
    git_checkout_command = ["git", "-C", "linux", "checkout", "-f", branch_tag]
    subprocess.run(git_checkout_command)
    
    result = subprocess.run(shell_command, shell=True, capture_output=True, text=True)
    shell_result = result.stdout.strip()
    
    print(f"Branch Tag: {branch_tag} | Shell Result: {shell_result}")
    # Write the results to the file
    output_file.write(f"Branch Tag: {branch_tag} | Shell Result: {shell_result}\n")

# Close the file
output_file.close()


