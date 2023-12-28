node_example = """
                9
                |
           -----------
           |         |
           8         5
           |         |
        -------   --------
        |     |   |      |
        7     6   4      3
               """

class Node:

    #Khởi tạo Contructor với giá trị(value), node trái(left), node phải(right)
    #Initialize the Contructor of Node with value, node left, node right
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    #Khi print ra sẽ hiện Node({giá trị})
    #When print the node, console will display Node({value})
    #Ex: Node(2)
    def __str__(self):
        return f"Node({self.value})"

#khởi tạo Cấu trúc Node
#Initialize the structure of Node
mytree = Node(9, Node(8, Node(7), Node(6)), Node(5, Node(4), Node(3)))

#In ra từng bước đi của cấu trúc Node
#Print out each step of the Node structure
def walk(tree):
    if tree is not None:
        #In ra node hiện tại
        #Print current node
        print(tree)
        #Tiếp tục in ra các node trái và phải
        #Continue to next node
        walk(tree.left)
        walk(tree.right)

#Tìm đường đi trong cấu trúc Node từ node đầu đến node đích(target)
#Find the path way in the structure from fisrt node to target node
def find_solution(current_node, target, path):

    #Nếu không có node trái và phải thì False
    #If not have any next node in node left and right
    if current_node is None:
        return False
    
    #Thêm node hiện tại vào mảng đường đi(path)
    #Add current node into path way
    path.append(current_node)
    

    #Nếu giá trị node hiện tại = target thì True
    #If value of current node = target -> True
    if current_node.value == target:
        return True
    
    #Nếu vẫn còn node trái hoặc phải thì sẽ kiểm tra tiếp
    #Nếu 1 trong 2 node trái hoặc phải = target thì True
    #If have node left or right, continue checking
    #If 1 of 2 node = target -> True
    if (find_solution(current_node.left, target, path) or
        find_solution(current_node.right, target, path)):
        return True
    
    #Nếu node đi đến cuối mà vẫn không = với target => xóa node đó khỏi path
    #If node from first to last not found target => Delete this node from path
    path.pop()
    return False

#Tìm đường đi đến đích của target
#Find path way
def walk_advance(tree, target):

    #Khởi tạo:
    #   Stack: chứa các node cần kiểm tra
    #   Solution: chứa đường đi đến target
    #   Path: đường đi hiện tại của node
    #Init:
    #   Stack: contains nodes which need to check
    #   Solution: contains path way to target
    #   Path: contains path way from current node
    stack = []
    solution = []
    path = []

    #Thêm node hiện tại vào stack
    #Add current node into stack
    stack.append(tree)

    #Nếu stack vẫn còn node
    #If stack has node
    while len(stack) > 0:

        #Đẩy node cuối trong stack ra ngoài để kiểm tra
        #Bring last node in stack to outside to check
        node = stack.pop()

        #Nếu hàm find_solution là True
        #Có nghĩa là đã tìm ra đường đi đến target
        #If find_solution function is True
        #It means had been found path way to target
        if find_solution(node, target, path):

            #Đưa path vào trong solution để in ra kết quả
            #Add path into solution to print out results
            solution.extend(path)

    return solution

result = walk_advance(mytree, 3)

for node in result:
    print(node)

#How to run code?
    #python maze.py [file maze txt]