import pyautogui
from PIL import ImageGrab, ImageOps

# https://trex-runner.com/

rep = (1280, 487)
dino = (982, 492, 1022, 534)
delta = 80
delta2 = 15


def imagegrab():
	bbox = (dino[0] + delta, dino[1], dino[2] + delta, dino[3] - delta2)
	img = ImageGrab.grab(bbox)
	grayimg = ImageOps.grayscale(img)
	# grayimg.save("target.jpg")
	b = grayimg.getcolors()
	a = sum(map(sum, grayimg.getcolors()))
	return a

# print(imagegrab())


def jump():
	pyautogui.keyDown('space')
	pyautogui.keyUp("space")


def restart():
	pyautogui.click(rep)


def main():
	restart()
	while True:
		imagegrab()
		if imagegrab() != 1327:
			jump()


if __name__ == "__main__":
	main()

