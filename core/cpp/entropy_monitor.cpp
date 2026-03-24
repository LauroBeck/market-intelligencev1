#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <map>

double calculate_entropy(const std::vector<double>& pct_moves) {
    double entropy = 0.0;
    std::map<int, int> frequencies;
    
    // Bin the moves to create a probability distribution
    for (double move : pct_moves) {
        int bin = static_cast<int>(std::round(move * 10)); // 0.1% bins
        frequencies[bin]++;
    }

    for (auto const& [bin, count] : frequencies) {
        double p = static_cast<double>(count) / pct_moves.size();
        if (p > 0) entropy -= p * std::log2(p);
    }
    return entropy;
}

int main() {
    // Percentage moves from 3:51 ET Final Ticks
    std::vector<double> session_moves = {-0.85, -0.39, -0.18, 5.36, 1.56, 1.92, 2.87};
    
    double h = calculate_entropy(session_moves);

    std::cout << "Global Market Decoherence Report | March 24, 2026" << std::endl;
    std::cout << "================================================" << std::endl;
    std::cout << "System Entropy (H): " << std::fixed << std::setprecision(4) << h << " bits" << std::endl;

    if (h < 2.0) {
        std::cout << "State: COHERENT (High Trend Persistence)" << std::endl;
        std::cout << "Projection: Sell-off likely to carry into Nikkei/Asia." << std::endl;
    } else {
        std::cout << "State: DECOHERENT (Trend Dissipation)" << std::endl;
        std::cout << "Projection: Expect mean-reversion or sideways overnight." << std::endl;
    }

    return 0;
}
