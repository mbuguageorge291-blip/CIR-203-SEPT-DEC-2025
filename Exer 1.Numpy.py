
import numpy as np

print("="*70)
print("BANKING TRANSACTION ANALYSIS - NUMPY ARRAYS")
print("="*70)
print()
print("TASK 1: Creating 2D Array of Transaction Volumes")
print("-"*70)
transaction_volumes = np.array([
    [1200, 1350, 1180, 1420, 1560, 1490],  # Branch 1
    [980, 1100, 1050, 1200, 1280, 1150],   # Branch 2
    [1450, 1520, 1380, 1650, 1720, 1680],  # Branch 3
    [1050, 1180, 1120, 1300, 1400, 1350]   # Branch 4
])

print("Transaction Volumes Array (4 branches x 6 months):")
print(transaction_volumes)
print()
print(f"Array Shape: {transaction_volumes.shape}")
print(f"Array Dimensions: {transaction_volumes.ndim}D")
print(f"Total Elements: {transaction_volumes.size}")
print(f"Data Type: {transaction_volumes.dtype}")
print()

# Display with labels for better understanding
print("\nFormatted View with Labels:")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
print(f"{'Branch':<10} {' '.join([f'{m:>8}' for m in months])}")
print("-"*70)
for i, row in enumerate(transaction_volumes, 1):
    print(f"Branch {i}   {' '.join([f'{val:>8}' for val in row])}")
print()
print("\n" + "="*70)
print("TASK 2: Total Transactions per Branch")
print("-"*70)

# Using sum along axis 1 (columns) to get sum for each row (branch)
total_per_branch = np.sum(transaction_volumes, axis=1)

print("Total transactions for each branch:")
for i, total in enumerate(total_per_branch, 1):
    print(f"Branch {i}: {total:,} transactions")

print(f"\nTotal Transactions Array: {total_per_branch}")
print()

# Additional statistics per branch
print("Additional Branch Statistics:")
print(f"{'Branch':<10} {'Total':>12} {'Average':>12} {'Min':>12} {'Max':>12}")
print("-"*70)
for i in range(len(transaction_volumes)):
    branch_data = transaction_volumes[i]
    print(f"Branch {i+1}   {np.sum(branch_data):>12,} "
          f"{np.mean(branch_data):>12.2f} "
          f"{np.min(branch_data):>12,} "
          f"{np.max(branch_data):>12,}")
print()

# ============================================================================
# TASK 3: Identify Branch with Highest Total Transactions (4 marks)
# ============================================================================
print("\n" + "="*70)
print("TASK 3: Branch with Highest Total Transactions")
print("-"*70)

# Find the index of maximum value
max_branch_index = np.argmax(total_per_branch)
max_transactions = total_per_branch[max_branch_index]

print(f"Branch with highest transactions: Branch {max_branch_index + 1}")
print(f"Total transactions: {max_transactions:,}")
print()

# Additional analysis
print("Ranking of Branches by Total Transactions:")
sorted_indices = np.argsort(total_per_branch)[::-1]  # Descending order
for rank, idx in enumerate(sorted_indices, 1):
    print(f"{rank}. Branch {idx+1}: {total_per_branch[idx]:,} transactions")
print()

# Performance comparison
avg_total = np.mean(total_per_branch)
print(f"Average total across branches: {avg_total:,.2f}")
print(f"Branch {max_branch_index + 1} exceeds average by: "
      f"{max_transactions - avg_total:,.2f} transactions "
      f"({((max_transactions/avg_total - 1) * 100):.2f}%)")
print()

print("\n" + "="*70)
print("TASK 4: Average Monthly Transaction Volume")
print("-"*70)

monthly_averages = np.mean(transaction_volumes, axis=0)

print("Average transaction volume per month (across all branches):")
for i, (month, avg) in enumerate(zip(months, monthly_averages)):
    print(f"{month}: {avg:,.2f} transactions")

print(f"\nMonthly Averages Array: {monthly_averages}")
print()

print("Overall Statistics:")
print(f"Overall average (all branches, all months): {np.mean(transaction_volumes):,.2f}")
print(f"Overall standard deviation: {np.std(transaction_volumes):,.2f}")
print(f"Overall minimum: {np.min(transaction_volumes):,}")
print(f"Overall maximum: {np.max(transaction_volumes):,}")
print(f"Overall total: {np.sum(transaction_volumes):,}")
print()

print("Trend Analysis:")
first_month_avg = monthly_averages[0]
last_month_avg = monthly_averages[-1]
growth = ((last_month_avg - first_month_avg) / first_month_avg) * 100
print(f"Growth from Jan to Jun: {growth:.2f}%")

# Identify best and worst performing months
best_month_idx = np.argmax(monthly_averages)
worst_month_idx = np.argmin(monthly_averages)
print(f"Best performing month: {months[best_month_idx]} ({monthly_averages[best_month_idx]:,.2f})")
print(f"Worst performing month: {months[worst_month_idx]} ({monthly_averages[worst_month_idx]:,.2f})")
print()

# ============================================================================
# TASK 5: Reshape Array to 3x8 Format (4 marks)
# ============================================================================
print("\n" + "="*70)
print("TASK 5: Reshaping Array to 3x8 Format")
print("-"*70)

# Reshape from 4x6 (24 elements) to 3x8 (24 elements)
reshaped_array = transaction_volumes.reshape(3, 8)

print("Original Array Shape: (4, 6) - 4 branches x 6 months")
print("Reshaped Array Shape: (3, 8) - 3 rows x 8 columns")
print()

print("Reshaped Array:")
print(reshaped_array)
print()


print("="*70)
print("IMPLICATIONS OF RESHAPING IN BANKING CONTEXT:")
print("="*70)
print()

print("1. DATA REORGANIZATION:")
print("   - Original: 4 branches × 6 months = 24 data points")
print("   - Reshaped: 3 rows × 8 columns = 24 data points (same total)")
print("   - The data is rearranged but no information is lost")
print()

print("2. BUSINESS INTERPRETATION CHANGES:")
print("   - Original format: Natural representation (branches vs months)")
print("   - Reshaped format: Could represent:")
print("     * 3 regions with 8 time periods (quarterly analysis)")
print("     * 3 quarters with 8 branches")
print("     * 3 product lines across 8 weeks")
print()

print("3. ANALYTICAL IMPLICATIONS:")
print("   - Different axis calculations yield different insights")
print("   - Row sums now represent different business metrics")
print("   - Column sums have different business meanings")
print()

# Demonstrate different insights from reshaped data
print("4. COMPARISON OF INSIGHTS:")
print()
print("   Original Array (4x6):")
print(f"   - Row sums (per branch): {total_per_branch}")
print(f"   - Column sums (per month): {np.sum(transaction_volumes, axis=0)}")
print()
print("   Reshaped Array (3x8):")
reshaped_row_sums = np.sum(reshaped_array, axis=1)
reshaped_col_sums = np.sum(reshaped_array, axis=0)
print(f"   - Row sums: {reshaped_row_sums}")
print(f"   - Column sums: {reshaped_col_sums}")
print()

print("5. PRACTICAL USE CASES:")
print("   - Quarterly reporting (3 quarters instead of 6 months)")
print("   - Regional consolidation (3 regions instead of 4 branches)")
print("   - Alternative time period analysis (8 periods instead of 6)")
print("   - Data visualization with different aspect ratios")
print()

print("6. IMPORTANT NOTES:")
print("   ✓ Reshaping preserves all data values")
print("   ✓ Order of elements changes but content remains the same")
print("   ✓ Must ensure total elements match (4×6 = 3×8 = 24)")
print("   ✗ Business meaning/interpretation is altered")
print("   ✗ Original relationships between branches and months are lost")
print()

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*70)
print("SUMMARY REPORT")
print("="*70)
print()
print(f"Total Branches Analyzed: {transaction_volumes.shape[0]}")
print(f"Analysis Period: {transaction_volumes.shape[1]} months")
print(f"Total Transactions: {np.sum(transaction_volumes):,}")
print(f"Best Performing Branch: Branch {max_branch_index + 1} "
      f"({max_transactions:,} transactions)")
print(f"Average Monthly Volume: {np.mean(monthly_averages):,.2f} transactions")
print(f"Growth Rate (Jan-Jun): {growth:.2f}%")
print()
print("="*70)
print("END OF ANALYSIS")
print("="*70)
