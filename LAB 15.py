import random  

class Node:  
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):  
        self.feature = feature  
        self.threshold = threshold  
        self.left = left  
        self.right = right  
        self.value = value  

def predict(tree, row):  
    if tree.value is not None:  
        return tree.value  
    if row[tree.feature] <= tree.threshold:  
        return predict(tree.left, row)  
    return predict(tree.right, row)  

def simple_tree():  
    return Node(feature=0, threshold=5.5, left=Node(value=0), right=Node(value=1))  

def main():  
    tree = simple_tree()  
    print("Enter a feature value:")  
    value = float(input())  
    label = predict(tree, [value])  
    print("Predicted Label:", label)  

if __name__ == "__main__":  
    main()  
