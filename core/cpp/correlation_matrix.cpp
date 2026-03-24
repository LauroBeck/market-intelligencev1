#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

double calculate_correlation(const std::vector<double>& x, const std::vector<double>& y) {
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0, sum_y2 = 0;
    int n = x.size();
    for (int i = 0; i < n; i++) {
        sum_x += x[i]; sum_y += y[i]; sum_xy += x[i] * y[i];
        sum_x2 += x[i] * x[i]; sum_y2 += y[i] * y[i];
    }
    double num = n * sum_xy - sum_x * sum_y;
    double den = std::sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y));
    return (den == 0) ? 0 : num / den;
}

int main() {
    std::vector<double> nasdaq = {21820.38, 21772.45, 21767.64, 21759.22};
    std::vector<double> yield = {3.85, 3.88, 3.90, 3.92};
    std::vector<double> vix = {26.32, 26.64, 26.87, 26.90};

    std::cout << "Final Session Audit | 2026-03-24" << std::endl;
    std::cout << "---------------------------------" << std::endl;
    std::cout << "NASDAQ/Yield Corr: " << std::fixed << std::setprecision(4) << calculate_correlation(nasdaq, yield) << std::endl;
    std::cout << "NASDAQ/VIX Corr:   " << calculate_correlation(nasdaq, vix) << std::endl;
    
    return 0;
}
