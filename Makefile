DIR := $(shell pwd)

clean:
	sudo rm -rf node_1/db/*
	sudo rm -rf node_1/keystore/*
	sudo rm -rf node_2/db/*
	sudo rm -rf node_2/keystore/*
	sudo rm -rf node_3/db/*
	sudo rm -rf node_3/keystore/*

