package main;

import "fmt";
func main() {
	var age int;
	fmt.Println("Enter age");
	fmt.Scanln(&age);

	switch{
	case age>=18 {
		fmt.Println("You can drive!");
	}
	case age==0{
		fmt.Println("The age is zero?")
	}
	case age<18 {
		fmt.Println("You can't drive.")
	}
	default {
		fmt.Println("Enter a valid age ")
	}
	}
}
