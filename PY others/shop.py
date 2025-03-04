""" Do'kon dastur """
ombor = ["olma", "gilos", "non", "apelsin"]
print(f"Assalomu aleykum, do'konimizga xush kelibsiz! \nBizning do'konda {len(ombor)} ta mahsulotlar bor:", end=" ")
for mahsulot in ombor:
    if mahsulot == ombor[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == ombor[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")

bor = []
yoq = []
son = int(input("\nNechta mahsulot xarid qilmoqchisiz: "))
for s in range(son):
    mahsulot = input(f"{s+1}- mahsulotni kiriting: ").lower()
    if mahsulot in ombor:
        bor.append(mahsulot)
    else:
        yoq.append(mahsulot)

print(f"Bizda bor mahsulotlar: ")
for mahsulot in bor:
    if mahsulot == bor[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == bor[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")



print(f"\nBizda yoq mahsulotlar: ")
for mahsulot in yoq:
    if mahsulot == yoq[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == yoq[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")

