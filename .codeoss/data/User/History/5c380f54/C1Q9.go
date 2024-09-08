package main;

import "fmt";
func main() {
	var age int;
	fmt.Println("Enter age");
	fmt.Scanln(&age);
	if (age>=18) {
		fmt.Println("You can drive!");
	} else if(age<18) {
		fmt.Println("You can't drive");
	} else{
		fmt.Println("nter a valid age");
	}
}
