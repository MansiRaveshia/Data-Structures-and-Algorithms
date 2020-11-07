import heapq
#prg1
heap = []
data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
for item in data:
    heapq.heappush(heap, item)

while heap:
    print(heapq.heappop(heap)[1])

#prg2
print()
results="""Christania Williams  11.80\n Marie-Josee Ta Lou    10.86\n Elaine Thompson          10.71\nTori Bowie               10.83\nShelly-Ann Fraser-Pryce  10.86\nEnglish Gardner          10.94\nMichelle-Lee Ahye        10.92\nDafne Schippers          10.90"""
print(results.splitlines())
top_3 = heapq.nsmallest(3,results.splitlines(),key=lambda x:[float(x.split()[-1])])
print("\n".join(top_3))