from trees import BinaryTree

def buildParseTress(fpexp):
    fplis = fpexp.split()
    pStack = []

    eTree = BinaryTree('')

    pStack.append(eTree)

    currentTree = eTree

    for i in fplis:
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in "+-*/":
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError ("Unknown Operator: " + i)

    return eTree

pt = buildParseTress (" ( 10 + 5 ) * 3 ")

print pt
