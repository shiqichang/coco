# 数据结构

## 一、链表

### 1. 递归反转整个链表

```java
ListNode reverse(ListNode head) {
    // base case
    if (head == null || head.next == null) return head;
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return head;
}
```

`reverse` 函数的定义：输入一个节点 `head`, 将以 `head` 为起点的链表反转，并返回反转后的头节点。

### 2. 反转链表前 N 个节点

```java
ListNode successor = null; // 后驱节点

// 反转以 head 为起点的 n 个节点，返回新的头节点
ListNode reverseN(ListNode head, int n) {
    if (n == 1) {
        // 记录第 n + 1 个节点
        successor = head.next;
        return head;
    }
    // 以 head.next 为起点，需要反转前 n - 1 个节点
    ListNode last = reverseN(head.next, n - 1);

    head.next.next = head;
    // 让反转之后的 head 节点和后面的节点连接起来
    head.next = successor;
    return last;
}
```

### 3. 反转链表的一部分

```java
ListNode successor = null;

ListNode reverseN(ListNode head, int n) {
    if (n == 1) {
        successor = head.next;
        return head;
    }
    ListNode last = reverseN(head.next, n - 1);

    head.next.next = head;
    head.next = successor;
    return last;
}

ListNode reverseBetween(ListNode head, int m, int n) {
    // base case
    if (m == 1) {
        return reverseN(head, n);
    }
    // 前进到反转的起点触发 base case
    head.next = reverseBetween(head.next, m - 1, n - 1);
    return head;
}
```

递归解法和迭代解法的时间复杂度都为 O(N)。但递归解法的空间复杂度为 O(N), 迭代解法的空间复杂度为 O(1).

### 4. K 个一组反转链表

迭代反转整个链表

```java
// 反转以 a 为头节点的链表
ListNode reverse(ListNode a) {
    ListNode pre, cur, nxt;
    pre = null; cur = a; nxt = a;
    while (cur != null) {
        nxt = cur.next;
        // 逐个节点反转
        cur.next = pre;
        // 更新指针位置
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头节点
    return pre;
}
```

反转 a 到 b 之间的节点

```java
/* 反转 [a, b) 的元素，注意是左闭右开 */
ListNode reverse(ListNode a, ListNode b) {
    ListNode pre, cur, nxt;
    pre = null; cur = a; nxt = a;
    // while 的终止条件改一下即可
    while (cur != b) {
        nxt = cur.next;
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头节点
    return pre;
}
```

`reverseKGroup` 函数

```java
ListNode reverseKGroup(ListNode head, int k) {
    if (head == null) return null;
    ListNode a, b;
    // 区间 [a, b) 包含 k 个待反转元素
    a = b = head;
    for (int i = 0; i < k; i++) {
        // 不足 k 个，不需要反转，base case
        if (b == null) return head;
        b = b.next;
    }
    // 反转前 k 个元素
    ListNode newHead = reverse(a, b);
    // 递归反转后续链表并连接起来
    a.next = reverseKGroup(b, k);
    return newHead;
}

ListNode reverse(ListNode a, ListNode b) {
    ListNode pre, cur, nxt;
    pre = null; cur = a; nxt = a;
    for (cur != b) {
        nxt = cur.next;
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}
```

### 5. 回文链表

寻找回文串

```c++
string palindrome(string& s, int l , int r) {
    // 防止索引越界
    while (l >= 0 && r < s.size() && s[l] == s[r]) {
        // 向两边扩展
        l--; r++;
    }
    // 返回以 s[l], s[r] 为中心的最长回文串
    return s.substr(l + 1, r - l - 1);
}
```

判断回文串，双指针法。

```c++
bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) 
            return false;
        left++; right--;
    }
    return true;
}
```

判断回文单链表

```java
// 左侧指针
ListNode left;

boolean isPalindrome(ListNode head) {
    left = head;
    return traverse(head);
}

boolean traverse(ListNode right) {
    if (right == null) return true;
    boolean res = traverse(right.next);
    // 后序遍历代码
    res = res && (right.val == left.val);
    left = left.next;
    return res;
}
```

优化空间复杂度

```java
boolean isPalindrome(ListNode head) {
    if (head == null) return true;

    // 找到前半部分链表的尾节点并反转后半部分链表
    ListNode firstHalfEnd = endOfFirstHalf(head);
    ListNode secondHalfStart = reverse(firstHalfEnd.next);

    // 判断是否回文
    ListNode p1 = head;
    ListNode p2 = secondHalfStart;
    boolean result = true;
    while (result && p2 != null) {
        if (p1.val != p2.val)
            result = false;
        p1 = p1.next;
        p2 = p2.next;
    }

    // 还原链表并返回结果
    firstHalfEnd.next = reverse(secondHalfStart);
    return result;
}

ListNode reverse(ListNode head) {
    ListNode pre = null, cur = head;
    while (cur != null) {
        ListNode nxt = cur.next;
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

ListNode endOfFirstHalf(ListNode head) {
    ListNode fast, slow;
    fast = slow = head;
    while (fast.next != null && fast.next.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
```

时间复杂度为 O(N), 空间复杂度为 O(1).

## 二、二叉树

### 1. 构建最大二叉树

```java
/* 主函数 */
TreeNode constructMaximumBinaryTree(int[] nums) {
    return build(nums, 0, nums.length - 1);
}

TreeNode build(int[] nums, int lo, int hi) {
    // base case
    if (lo > hi) return null;

    // 找到数组中最大的值和对应的索引
    int index = -1, maxVal = Integer.MIN_VALUE;
    for (int i = lo; i <= hi; i++) {
        if (nums[i] > maxVal) {
            index = i;
            maxVal = nums[i];
        }
    }

    TreeNode root = new TreeNode(maxVal);
    // 递归调用构造左右子树
    root.left = build(nums, lo, index - 1);
    root.right = build(nums, index + 1, hi);

    return root;
}
```

### 2. 通过前序和中序遍历结果构造二叉树

前序遍历、中序遍历、后序遍历

```java
void traverse(TreeNode root) {
    // 前序遍历
    preorder.add(root.val);
    traverse(root.left);
    traverse(root.right);
}

void traverse(TreeNode root) {
    traverse(root.left);
    // 中序遍历
    inorder.add(root.val);
    traverse(root.right);
}

void traverse(TreeNode root) {
    traverse(root.left);
    traverse(root.right);
    // 后序遍历
    postorder.add(root.val);
}
```

```java
/* 主函数 */
TreeNode buildTree(int[] preorder, int[] inorder) {
    return build(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
}

/*
    若前序遍历数组为 preorder[preStart..preEnd],
    中序遍历数组为 inorder[inStart..inEnd],
    构造二叉树，返回该二叉树的根节点
*/
TreeNode build(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, in inEnd) {
    // base case
    if (preStart > preEnd) {
        return null;
    }

    // root 节点对应的值就是前序遍历数组的第一个元素
    int rootVal = preorder[preStart];
    // rootVal 在中序遍历数组中的索引
    int index = 0;
    for (int i = inStart; i <= inEnd; i++) {
        if (inorder[i] == rootVal) {
            index = i;
            break;
        }
    }

    int leftSize = index - inStart;

    // 先构造出当前根节点
    TreeNode root = new TreeNode(rootVal);
    // 递归构造左右子树
    root.left = build(preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1);
    root.right = build(preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd);
    return root;
}
```

### 3. 通过中序和后序遍历结果构造二叉树

```java
TreeNode buildTree(int[] inorder, int[] postorder) {
    return build(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
}

TreeNode build(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) {
    if (inStart > inEnd) return null;

    int rootVal = postorder[postEnd];
    int index = 0;
    for (int i = inStart; i <= inEnd; i++) {
        if (inorder[i] == rootVal) {
            index = i;
            break;
        }
    }

    int leftSize = index - inStart;
    
    TreeNode root = new TreeNode(rootVal);
    root.left = build(inorder, inStart, index - 1, postorder, postStart, postStart + leftSize - 1);
    root.right = build(inorder, index + 1, inEnd, postorder, postStart + leftSize, postEnd - 1);
    return root;
}
```

### 4. 寻找重复子树

计算一棵二叉树的节点数

```java
int count(TreeNode root) {
    if (root == null) return 0;

    int left = count(root.left);
    int right = count(root.right);
    /**** 后序遍历位置 ****/
    int res = left + right + 1;
    return res;
}
```

```java
// 记录所有子树及出现的次数
HashMap<String, Integer> memo = new HashMap<>();
// 记录重复的子树根节点
LinkedList<TreeNode> res = new LinkedList<>();

/* 主函数 */
List<TreeNode> findDuplicateSubtrees(TreeNode root) {
    traverse(root);
    return res;
}

/* 辅助函数 */
String traverse(TreeNode root) {
    if (root == null) return "#";

    String left = traverse(root.left);
    String right = traverse(root.right);

    String subTree = left + "," + right + "," + root.val;
    
    int freq = memo.getOrDefault(subTree, 0);
    // 多次重复也只会被加入结果集一次
    if (freq == 1) {
        res.add(root);
    }
    // 给子树对应的出现次数加一
    memo.put(subTree, freq + 1);
    return subTree;
}
```

### 5. 寻找第 K 小的元素

二叉搜索树 BST 的中序遍历结果是有序的。（升序）

```java
int kthSmallest(TreeNode root, int k) {
    // 利用 BST 的中序遍历特性
    traverse(root, k);
    return res;
}

// 记录结果
int res = 0;
// 记录当前元素的排名
int rank = 0;

void traverse(TreeNode root, int k) {
    if (root == null) return;

    traverse(root.left, k);
    /**** 中序遍历位置 ****/
    rank++;
    if (k == rank) {
        // 找到第 k 小的元素
        res = root.val;
        return;
    }
    /*******************/
    traverse(root.right, k);
}
```

红黑树：改良的自平衡 BST, 增删改查都是 O(logN) 的复杂度。

### 6. BST 转化累加数

累加和是计算大于等于当前值的所有元素之和。利用 BST 中序遍历的降序顺序。

```java
TreeNode convertBST(TreeNode root) {
    traverse(root);
    return root;
}

// 记录累加和
int sum = 0

void traverse(TreeNode root) {
    if (root == null) return;

    traverse(root.right);
    // 维护累加和
    sum += root.val;
    // 将 BST 转化成累加树
    root.val = sum;
    traverse(root.left);
}
```

### 7. 判断 BST 的合法性

```java
boolean isValidBST(TreeNode root) {
    return isValidBST(root, null, null);
}

/* 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val */
boolean isValidBST(TreeNode root, TreeNode min, TreeNode max) {
    // base case
    if (root == null) return true;
    // 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
    if (min != null && root.val <= min.val) return false;
    if (max != null && root.val >= max.val) return false;
    // 限定左子树的最大值是 root.val, 右子树的最小值是 root.val
    return isValidBST(root.left, min, root) && isValidBST(root.right, root, max);
}
```

### 8. 在 BST 中搜索一个数

```java
boolean isInBST(TreeNode root, int target) {
    if (root == null) return false;
    if (root.val == target)
        return true;
    if (root.val < target)
        return isInBST(root.right, target);
    if (root.val > target)
        return isInBST(root.left, target);
}
```

```java
TreeNode searchBST(TreeNode root, int val) {
    if (root == null || root.val == val) return root;

    return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
}
```

### 9. 在 BST 中插入一个数

```java
TreeNode insertIntoBST(TreeNode root, int val) {
    if (root == null) return new TreeNode(root);
    if (root.val < val)
        root.right = insertIntoBST(root.right, val);
    if (root.val > val)
        root.left = insertIntoBST(root.left, val);
    return root;
}
```

### 10. 在 BST 中删除一个数

```java
TreeNode deleteNode(TreeNode root, int key) {
    if (root == null) return null;
    if (root.val == key) {
        // 这两个 if 把情况 1 和 2 都正确处理了
        if (root.right == null) return root.left;
        if (root.left == null) return root.right;
        // 处理情况 3
        TreeNode minNode = getMin(root.right);
        root.val = minNode.val;
        root.right = deleteNode(root.right, minNode.val);
    } else if (root.val < key) {
        root.right = deleteNode(root.right, key);
    } else if (root.val > key) {
        root.left = deleteNode(root.left, key);
    }
    return root;
}

TreeNode getMin(TreeNode node) {
    // BST 最左边的就是最小的
    while (node.left != null) node = node.left;
    return node;
}
```

### 11. 二叉树的序列化与反序列化

#### a. 前序遍历解法

```java
// 代表分隔符的字符
String SEP = ",";
// 代表 null 空指针的字符
String NULL = "#";

/* 主函数：将二叉树序列化为字符串 */
String serialize(TreeNode root) {
    // 用于拼接字符串
    StringBuilder sb = new StringBuilder();
    serialize(root, sb);
    return sb.toString();
}

/* 辅助函数：将二叉树存入 StringBuilder */
void serialize(TreeNode root, StringBuilder sb) {
    if (root == null) {
        sb.append(NULL).append(SEP);
        return;
    }

    /**** 前序遍历位置 ****/
    sb.append(root.val).append(SEP);
    /*******************/

    serialize(root.left, sb);
    serialize(root.right, sb);
}

/* 主函数：将字符串反序列化为二叉树结构 */
TreeNode deserialize(String data) {
    // 将字符串转化为列表
    LinkedList<String> nodes = new LinkedList<>();
    for (String s : data.split(SEP)) {
        nodes.addLast(s);
    }
    return deserialize(nodes);
}

/* 辅助函数：通过 nodes 列表构造二叉树 */
TreeNode deserialize(LinkedList<String> nodes) {
    if (nodes.isEmpty()) return null;

    /**** 前序遍历位置 ****/
    // 列表最左侧就是根节点
    String first = nodes.removeFirst();
    if (first.equals(NULL)) return null;
    TreeNode root = new TreeNode(Integer.parseInt(first));
    /*******************/

    root.left = deserialize(nodes);
    root.right = deserialize(nodes);

    return root;
}
```

#### b. 后序遍历解法

```java
String SEP = ",";
String NULL = "#";

String serialize(TreeNode root) {
    StringBuilder sb = new StringBuilder();
    serialize(root, sb);

    return sb.toString();
}

void serialize(TreeNode root, StringBuilder sb) {
    if (root == null) {
        sb.append(NULL).append(SEP);
        return;
    }

    serialize(root.left, sb);
    serialize(root.right, sb);

    /**** 后序遍历位置 ****/
    sb.append(root.val).append(SEP);
    /*******************/
}

TreeNode deserialize(String data) {
    LinkedList<String> nodes = new LinkedList<>();
    for (String s : data.split(SEP))
        nodes.addLast(s);
    
    return deserialize(nodes);
}

TreeNode deserialize(LinkedList<String> nodes) {
    if (nodes.isEmpty()) return null;

    // 从后向前取出元素
    String last = nodes.removeLast();
    if (last.equals(NULL)) return null;
    TreeNode root = new TreeNode(Integer.parseInt(last));
    
    // 先构造右子树，再构造左子树
    root.right = deserialize(nodes);
    root.left = deserialize(nodes);
    
    return root;
}
```

#### c. 中序遍历解法

中序遍历的方式行不通，因为无法实现反序列化方法 `deserialize` .

#### d. 层序遍历解法

层序遍历二叉树

```java
void traverse(TreeNode root) {
    if (root == null) return;

    // 初始化队列，将 root 加入队列
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    while (!q.isEmpty()) {
        TreeNode cur = q.poll();

        /**** 层序遍历位置 ****/
        System.out.println(root.val);
        /*******************/

        if (cur.left != null) {
            q.offer(cur.left);
        }
        if (cur.right != null) {
            q.offer(cur.right);
        }
    }
}
```

```java
String SEP = ",";
String NULL = "#";

String serialize(TreeNode root) {
    if (root == null) return "";
    StringBuilder sb = new StringBuilder();
    // 初始化队列，将 root 将入队列
    Queue<String> q = new LinkedList<>();
    q.offer(root);
    
    while (!q.isEmpty()) {
        TreeNode cur = q.poll();

        /**** 层序遍历位置 ****/
        if (cur == null) {
            sb.append(NULL).append(SEP);
            continue;
        }
        sb.append(cur.val).append(SEP);
        /*******************/

        q.offer(cur.left);
        q.offer(cur.right);
    }

    return sb.toString();
}

TreeNode deserialize(String data) {
    if (data.isEmpty()) return null;
    String[] nodes = data.split(SEP);
    TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));

    Queue<String> q = new LinkedList<>();
    q.offer(root);

    for (int i = 1; i < nodes.length;) {
        TreeNode parent = q.poll();

        String left = nodes[i++];
        if (!left.equals(NULL)) {
            parent.left = new TreeNode(Integer.parseInt(left));
            q.offer(parent.left);
        } else {
            parent.left = null;
        }

        String right = nodes[i++];
        if (!right.equals(NULL)) {
            parent.right = new TreeNode(Integer.parseInt(right));
            q.offer(parent.right);
        } else {
            parent.right = null;
        }
    }
    
    return root;
}
```

### 12. 扁平化嵌套列表迭代器

`NestedInteger` 数据结构：这个结构中存的数据可能是一个 `Integer` 整数，也可能是一个 `NestedInteger` 列表。

```java
public class NestedInteger {
    // 如果其中存的是一个整数，则返回 true, 否则返回 false
    public boolean isInteger();

    // 如果其中存的是一个整数，则返回这个整数，否则返回 null
    public Integer getInteger();

    // 如果其中存的是一个列表，则返回这个列表，否则返回 null
    public List<NestedInteger> getList();
}

public class NestedIterator implements Iterator<Integer> {
    // 构造器输入一个 NestedInteger 列表
    public NestedIterator(List<NestedInteger> nestedList) {};

    // 返回下一个整数
    public Integer next() {};

    // 是否还有下一个整数？
    public boolean hasNext() {};
}
```

先调用 `hasNext` 方法，再调用 `next` 方法。

`You should not implement it, or speculate abount its implemetation.`

```java
public class NestedInteger {
    private Integer val;
    private List<NestedInteger> list;

    public NestedInteger(Integer val) {
        this.val = val;
        this.list = null;
    }

    public NestedInteger(List<NestedInteger> list) {
        this.list = list;
        this.val = val;
    }

    public boolean isInteger() {
        return this.val != null;
    }

    public Integer getInteger() {
        return this.val;
    }

    public List<NestedInteger> getList() {
        return this.list;
    }
}

/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}
```

遍历一颗 N 叉树的所有叶子节点。

```java
class NestedIterator implements Iterator<Integer> {
    private Iterator<Integer> it;

    public NestedIterator(List<NestedInteger> nestedList) {
        // 存放 nestedList 打平的结果
        List<Integer> result = new LinkedList<>();
        for (NestedInteger node : nestedList) {
            // 以每个节点为根遍历
            traverse(node, result);
        }
        // 得到 result 列表的迭代器
        this.it = result.iterator();
    }

    public Integer next() {
        return it.next();
    }

    public boolean hasNext() {
        return it.hasNext();
    }

    // 遍历以 root 为根的多叉树，将叶子节点的值加入 result 列表
    private void traverse(NestedInteger root, List<Integer> result) {
        if (root.isInteger()) {
            // 到达叶子节点
            result.add(root.getInteger());
            return;
        }
        // 遍历框架
        for (NestedInteger child : root.getChild()) {
            traverse(child, result);
        }
    }
}
```

```java
class NestedIterator implements Iterator<Integer> {
    private LinkedList<NestedInteger> list;

    public NestedIterator(List<NestedInteger> nestedList) {
        // 不直接用 nestedList 的引用，是因为不能确定它的底层实现
        // 必须保证 LinkedList, 否则下面的 addFirst 会很低效
        list = new LinkedList<>(nestedList);
    }

    public Integer next() {
        // hasNext 方法保证了第一个元素一定是整数类型
        return list.remove(0).getInteger();
    }

    public boolean hasNext() {
        // 循环拆分列表元素，直到列表第一个元素是整数类型
        while (!list.isEmpty() && !list.get(0).isInteger()) {
            // 当列表开头第一个元素是列表类型时，进入循环
            List<NestedInteger> first = list.remove(0).getList();
            // 将第一个列表打平并按顺序添加到开头
            for (int i = first.size() - 1; i >= 0; i--) {
                list.addFirst(first.get(i));
            }
        }
        return !list.isEmpty();
    }
}
```

### 13. 最近公共祖先

Lowest Common Ancestor, 简称 LCA.

`git rebase master`

二叉树的最近公共祖先

```java
TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    // 两种情况的 base case
    if (root == null) return null;
    if (root == p || root == q) return root;

    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);
    // 情况 1
    if (left != null && right != null) {
        return root;
    }
    // 情况 2
    if (left == null && right == null) {
        return null;
    }
    // 情况 3
    return left == null ? right : left;
}
```

二叉树的后序遍。

### 14. 完全二叉树的节点数

- 完全二叉树: `Complete Binary Tree`
- 满二叉树: `Perfect Binary Tree`
- `Full Binary Tree`

普通二叉树

```java
int countNodes(TreeNode root) {
    if (root == null) return 0;
    return 1 + countNodes(root.left) + countNodes(root.right);
}
```

满二叉树，节点总数和树的高度呈指数关系。

```java
int countNodes(TreeNode root) {
    int h = 0;
    // 计算树的高度
    while (root != null) {
        root = root.left;
        h++;
    }
    // 节点总数就是 2^h - 1
    return (int)Math.pow(2, h) - 1;
}
```

完全二叉树。

```java
int countNodes(TreeNode root) {
    TreeNode l = root, r = root;
    // 记录左、右子树的高度
    int hl = 0, hr = 0;
    while (l != null) {
        l = l.left;
        hl++;
    }
    while (r != null) {
        r = r.right;
        hr++;
    }
    // 如果左右子树的高度相同，则是一颗满二叉树
    if (hl == hr) {
        return (int)Math.pow(2, hl) - 1;
    }
    // 如果左右子树高度不同，则按照普通二叉树的逻辑计算
    return 1 + countNodes(root.left) + countNodes(root.right);
}
```

## 三、数据结构

### 1. Union-Find 算法

并查集算法。

```java
class UF {
    /* 将 p 和 q 连接 */
    public void union(int p, int q);
    /* 判断 p 和 q 是否连通 */
    public boolean connected(int p, int q);
    /* 返回图中有多少个连通分量 */
    public int count();
}
```

连通：自反性、对称性、传递性。

```java
class UF {
    // 记录连通分量
    private int count;
    // 存储一棵树
    // 节点 x 的根节点是 parent[x]
    private int[] parent;
    // 新增一个数组记录树的“重量”
    private int[] size;

    /* 构造函数，n 为图的节点总数 */
    public UF(int n) {
        // 一开始互不连通
        this.count = n;
        // 父节点指针初始指向自己
        // 最初每棵树只有一个节点
        // 重量应该初始化 1
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;

        // 将两棵树合并为一棵
        // 小树接到大树下面，较平衡
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        // parent[rootQ] = rootP 也一样
        count--; // 两个分量合二为一
    }

    /* 返回某个节点 x 的根节点 */
    private int find(int x) {
        // 根节点 parent[x] == x
        while (parent[x] != x) {
            // 进行路径压缩
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    /* 返回当前的连通分量个数 */
    public int count() {
        return count;
    }

    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }
}
```

`find`, `union`, `connected` 的时间复杂度都为 `O(1)`.

- `parent` 数组内实际存储着一个森林（若干棵多叉树）；
- `size` 数组记录着每棵树的重量，拥有平衡性；
- `find` 函数中进行路径压缩，保证任意树的高度保持在常数。

### 2. DFS 的替代方案

**将二维坐标映射到一维的常见技巧**：二维坐标 `(x,y)` 可以转换为 `x * n + y` 这个数（`m` 是棋盘的行数，`n` 是棋盘的列数。）

```java
void solve(char[][] board) {
    if (board.length == 0) return;

    int m = board.length;
    int n = board[0].length;
    // 给 dummy 留一个额外位置
    UF uf = new UF(m * n + 1);
    int dummy = m * n;
    // 将首列与末列的 O 与 dummy 连通
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O')
            uf.union(i * n, dummy);
        if (board[i][n - 1] == 'O')
            uf.union(i * n + n - 1, dummy);
    }
    // 将首行与某行的 O 与 dummy 连通
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O')
            uf.union(j, dummy);
        if (board[m - 1][j] == 'O')
            uf.union((m - 1) * n + j, dummy);
    }
    // 方向数组 d 是上下左右搜索的常见手法
    int[][] d = new int[][]{{1, 0}, {0, 1}, {0, -1}, {-1, 0}};
    for (int i = 1; i < m - 1; i++)
        for (int j = 1; j < n - 1; j++)
            if (board[i][j] == 'O')
                for (int k = 0; k < 4; k++) {
                    int x = i + d[k][0];
                    int y = j + d[k][1];
                    if (board[x][y] == 'O')
                        uf.union(x * n + y, i * n + j);
                }
    // 所有不和 dummy 连通的 O, 都要被替换
    for (int i = 1; i < m - 1; i++)
        for (int j = 1; j < n - 1; j++)
            if (!uf.connected(dummy, i * n + j))
                board[i][j] = 'X';
}
```

**主要思路是适时增加虚拟节点，想办法让元素分门别类，建立动态连通关系。**

### 3. 判断合法等式

核心思想：将 `equations` 中的算式根据 `==` 和 `!=` 分成两部分，先处理 `==` 算式，使得他们通过想等关系各自勾结成门派；然后再处理 `!=` 算式，检查不等关系是否破坏了想等关系的连通性。

```java
boolean equationsPossible(String[] equations) {
    UF uf = new UF(26); // 26 个英文字母

    // 先让想等的字母形成连通分量
    for (String eq : equations) {
        if (eq.charAt(1) == '=') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            uf.union(x - 'a', y - 'a');
        }
    }
    // 检查不等关系是否打破想等关系的连通性
    for (String eq : equations) {
        if (eq.charAt(1) == '!') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            // 如果想等关系成立，就是逻辑冲突
            if (uf.connected(x - 'a', y - 'a'))
                return false;
        }
    }
    return true;
}
```

### 4. LRU 算法

LRU 算法是一种缓存淘汰机制。(Least Recently Used), 核心数据结构是哈希链表，双向链表和哈希表的结合体。

```java
class DoubleList {
    // 头尾虚节点
    private Node head, tail;
    // 链表元素数
    private int size;

    public DoubleList() {
        // 初始化双向链表的数据
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    // 在链表尾部添加节点 x, 时间 O(1)
    public void add(Node x) {
        x.prev = tail.prev;
        x.next = tail;
        tail.prev.next = x;
        tail.prev = x;
        size++;
    }

    // 删除链表中的 x 节点（x 一定存在）
    // 由于是双向链表且给的是目标 Node 节点，时间 O(1)
    public void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
        size--;
    }

    // 删除链表中第一个节点，并返回该节点，时间 O(1)
    public Node removeFirst() {
        if (head.next == tail) return null;

        Node first = head.next;
        remove(first);
        return first;
    }

    // 返回链表长度，时间 O(1)
    public int size() {
        return size;
    }
}
```

靠尾部的数据是最近使用的，靠头部的是最久未使用的。

```java
class LRUCache {
    int cap;
    LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>();

    public LRUCache(int capacity) {
        this.cap = capacity;
    }

    public int get(int key) {
        if (!cache.containsKey(key))
            return -1;
        // 将 key 变为最近使用
        makeRecently(key);
        return cache.get(key);
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            // 修改 key 的值
            cache.put(key, val);
            // 将 key 变为最近使用
            makeRecently(key);
            return;
        }

        if (cache.size >= this.cap) {
            // 链表头部就是最久未使用的 key
            int oldestKey = cache.keySet().iterator().next();
            cache.remove(oldestKey);
        }
        // 将新的 key 添加链表尾部
        cache.put(key, val);
    }

    private void makeRecently(int key) {
        int val = cache.get(key);
        // 删除 key, 重新插入到队尾
        cache.remove(key);
        cache.put(key, val);
    }
}
```

### 5. LFU 算法

```java

```

### 6. 数据流的中位数

```java

```

### 7. 设计朋友圈时间线功能

```java

```

### 8. 单调栈

单调栈只处理一种典型问题: `Next Greater Element`.

#### a. 单调栈模板

```c++
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> res(nums.size()); // 存放答案的数组
    stack<int> s;
    // 倒着往栈里放
    for (int i = nums.size() - 1; i >= 0; i--) {
        // 判断个子高矮
        while (!s.empty() && s.top() <= nums[i]) {
            s.pop(); // 矮个起开
        }
        res[i] = s.empty() ? -1 : s.top();
        s.push(nums[i]);
    }
    return s;
}
```

下一个更大元素 I

```java
public int[] nextGreaterElement(int[] findNums, int[] nums) {
    stack<Integer> stack = new stack<>();
    HashMap<Integer, Integer> map = HashMap<>();
    int[] res = new int[findNums.length];
    for (int i = 0; i < nums.length; i++) {
        while (!stack.empty() && nums[i] > stack.peek()) {
            map.put(stack.pop(), nums[i]);
        }
        stack.push(nums[i]);
    }
    while (!stack.empty()) {
        map.put(stack.pop(), -1);
    }
    for (int i = 0; i < findNums.length; i++) {
        res[i] = map.get(findNums[i]);
    }
    return res;
}
```

#### b. 问题变形

```c++
vector<int> dailyTemperatures(vector<int>& T) {
    vector<int> res(T.size());
    stack<int> s;
    for (int i = T.size() - 1; i >= 0; i--) {
        while (!s.empty() && T[s.top()] <= T[i]) {
            s.pop();
        }
        res[i] = s.empty() ? 0 : (s.top() - i);
        s.push(i);
    }
    return res;
}
```

#### c. 处理环形数组

下一个更大元素 II

```c++
vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n);
    stack<int> s;
    // 假装这个数组长度翻倍了
    for (int i = 2 * n - 1; i >= 0; i--) {
        // 索引要求模，其他的和模板一样
        while (!s.empty() && s.top() <= nums[i % n])
            s.pop();
        res[i % n] = s.empty() ? -1 : s.top();
        s.push(nums[i % n]);
    }
    return res;
}
```

官方解法

```c++
vector<int> nextGreatorElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> s;
    for (int i = 0; i < n * 2 - 1; i++) {
        while (!s.empty() && nums[s.top()] < nums[i % n]) {
            res[s.top()] = nums[i % n];
            s.pop();
        }
        s.push(i % n);
    }
    return res;
}
```

### 9. 单调队列

队列中的元素全都是单调递增（或递减）的。
