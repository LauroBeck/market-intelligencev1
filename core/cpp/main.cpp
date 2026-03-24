#include <iostream>
#include <string>
#include <iomanip>
#include <vector>

struct MarketTick {
    std::string symbol;
    double price;
    double pct_change;
};

int main() {
    // 3:48 ET Closing Data
    MarketTick nasdaq = {"NASDAQ", 21767.64, -0.82};
    std::vector<MarketTick> fx = {
        {"GBP-USD", 1.3384, -0.34},
        {"USD-CAD", 1.3763, 0.34},
        {"USD-CNY", 6.8930, 0.14}
    };

    std::cout << "Bloomberg Final Bell Analysis | 2026-03-24" << std::endl;
    std::cout << "===========================================" << std::endl;
    std::cout << "NASDAQ Status: " << nasdaq.price << " (" << nasdaq.pct_change << "%)" << std::endl;
    std::cout << "-------------------------------------------" << std::endl;

    for (const auto& tick : fx) {
        std::cout << std::left << std::setw(10) << tick.symbol 
                  << " | Price: " << std::setw(8) << tick.price 
                  << " | Move: " << (tick.pct_change > 0 ? "+" : "") << tick.pct_change << "%" << std::endl;
    }
    
    return 0;
}
