from math import radians,sin,cos,tan

angulo = float(input("Digite o valor do angulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print("O ângulo de {} tem o SENO {:.2f}".format(angulo,sen))
print("O ângulo de {} tem o COSSENO {:.2f}".format(angulo,cos))
print("O ângulo de {} tem a TANGENTE {:.2f}".format(angulo,tan))