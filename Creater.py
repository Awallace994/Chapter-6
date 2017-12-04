Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> zombies = int(input("Enter the number of zombies: "))
Enter the number of zombies: 22
>>> if zombies > 20:
	print("That's a lot of zombies. ")

	
That's a lot of zombies. 
>>> zombies = 5
>>> zombies = 22
>>> password = "cats"
>>> attempt = input("Please enter the password: ")
Please enter the password: cats
>>> if attempt == password:
	print("Password is correct")
	print("Program finished")

	
Password is correct
Program finished
>>> attempt == password
True
>>> attempt = input("Please enter the password: ")
Please enter the password: cats
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> answer = input("Create a crater? Y/N ")
Create a crater? Y/N yes
>>> if attempt == yes
SyntaxError: invalid syntax
>>> if attempt == true
SyntaxError: invalid syntax
>>> if attempt == Y
SyntaxError: invalid syntax
>>> >=if answer == Y:
	
SyntaxError: invalid syntax
>>> if answer == Y:
	print("Answer accepted")
	print("Running program")

	
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    if answer == Y:
NameError: name 'Y' is not defined
>>> Y = yes
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Y = yes
NameError: name 'yes' is not defined
>>> Y = 1
>>> pos = mc.player.getPos()
>>> mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
>>> mc.postToChat("Boom!")
>>> var = variable = y = 10
>>> var
10
>>> variable
10
>>> y
10
>>> answer = input("Create a crater? Y/N ")
Create a crater? Y/N Y
>>> mc.postToChat = (answer + Y)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    mc.postToChat = (answer + Y)
TypeError: Can't convert 'int' object to str implicitly
>>> mc.postToChat(answer + "Yes")
>>> Blocks = mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
>>> if Blocks == true
SyntaxError: invalid syntax
>>> if Blocks = true
SyntaxError: invalid syntax
>>> if crater = mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
SyntaxError: invalid syntax
>>> crater = mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
>>> answer + "y" = mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
SyntaxError: can't assign to operator
>>> Y = mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
>>> answer = input("Create a crater? Y/N ")
Create a crater? Y/N Y
>>> 
