idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura(em metros): "))
peso = float(input("Informe seu peso(em kg): "))

imc = peso / (altura * altura)

print(imc)

if (imc < 18.5):{
	print("abaixo do peso")
}
elif (imc < 24.9):{
	print("peso saudável")
}
elif (imc < 29.9):{
	print("sobrepeso")
}
elif (imc < 39.9):{
	print("obeso")
}
elif (imc > 40):{
	print("obeso mórbido")
}
