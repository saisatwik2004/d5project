from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score

# Hardcoded example labels
y_true = ['Alice', 'Bob', 'Unknown', 'Alice', 'Eve']
y_pred = ['Alice', 'Bob', 'Eve', 'Unknown', 'Eve']

labels = sorted(list(set(y_true + y_pred)))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred, labels=labels))

# Classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, labels=labels))

# Precision, Recall, F1
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

print(f"\nPrecision: {precision*100:.2f}%")
print(f"Recall: {recall*100:.2f}%")
print(f"F1-Score: {f1*100:.2f}%")
