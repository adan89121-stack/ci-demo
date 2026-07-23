# PR Review Demo 範例

這是一個很適合拿來展示「PR 查核」效果的簡單案例。

## 1. 建議的 Demo 內容

把這個 PR 內容當成一個有明顯問題的變更，讓 review bot 產生評論：

- 硬編碼 API Key
- 除以 0 時可能造成 crash
- 缺少基本的錯誤處理

## 2. 範例變更

假設在 [test.py](test.py) 裡做了以下修改：

```python
API_KEY = "sk-test-1234567890"

def divide(a, b):
    return a / b
```

這段程式看起來很簡單，但實際上有兩個明顯問題：

1. `API_KEY` 是硬編碼密鑰，屬於資訊安全風險。
2. `divide(a, b)` 沒有處理 `b == 0`，會在執行時丟出錯誤。

## 3. 適合展示的 Review 內容

PR 查核工具應該會針對這些點給出建議：

### 可能的 review 意見

- 「請避免在程式碼中硬編碼 API Key，建議改從環境變數或 Secret Manager 讀取。」
- 「當分母為 0 時，這段邏輯會造成例外，建議加入檢查與明確錯誤訊息。」
- 「建議增加單元測試，覆蓋 `b = 0` 的情況。」

## 4. 可直接拿來演示的中文範例回覆

```text
這次 PR 的主要變更是新增了一個簡單的除法函式，然而有幾個值得注意的問題：

1. 硬編碼 API Key：目前程式碼中直接寫入了 API Key，這會增加資訊外洩風險。
2. 除以 0 的邏輯漏洞：當傳入分母為 0 時，會導致執行錯誤，建議加入檢查並回傳清楚的錯誤訊息。
3. 缺少測試覆蓋：建議補上針對 `b = 0` 的測試案例。

建議修正方式如下：

```python
import os

API_KEY = os.getenv("API_KEY")


def divide(a, b):
    if b == 0:
        raise ValueError("分母不能為 0")
    return a / b
```
```

## 5. 為什麼這個例子好

這個例子很適合做 demo，因為它很容易看懂，而且剛好涵蓋到 PR review 常見的三個面向：

- 安全性
- 邏輯正確性
- 可維護性

## 6. 更推薦的 Demo 範例：SQL Injection

如果你想要讓 demo 更有「正式 PR review」感，我會更推薦下面這個例子。它比單純的除法函式更像真實系統中的風險點。

### 範例程式碼

```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query
```

### 為什麼這個例子更好

- 這是非常典型的安全性問題。
- AI reviewer 很容易給出明確建議：改用參數化查詢。
- 觀眾一看就知道這是「會造成資料庫查詢注入」的風險。

### 可展示的 review 意見

- 「這段 SQL 直接字串拼接，存在 SQL Injection 風險。」
- 「建議改用參數化查詢，例如 `cursor.execute("SELECT * FROM users WHERE username = %s", (username,))`。」
- 「建議補上輸入驗證與測試案例。」

### 修正範例

```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    return query
```

## 7. 如果你想要更像產品實戰的版本

你也可以把 demo 做成這三種風格之一：

1. 安全性為主：SQL Injection、硬編碼密鑰、未驗證輸入
2. 邏輯為主：除以 0、空值處理、邊界條件
3. 維護性為主：重複程式碼、低可讀性、缺少測試

如果你要的是「最容易讓觀眾看懂」的版本，我建議選擇：

- 第一優先：SQL Injection
- 第二優先：硬編碼 API Key
- 第三優先：除以 0 的錯誤處理
