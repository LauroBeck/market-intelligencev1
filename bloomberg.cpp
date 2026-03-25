#include <iostream>
#include <string>
#include <iomanip>

void print_header(std::string ticker) {
    std::cout << "\033[1;37;42m " << ticker << " US Equity \033[0m" 
              << " \033[1;32mMarket Open - Velocity Active\033[0m" << std::endl;
}

int main(int argc, char* argv[]) {
    std::string ticker = (argc > 1) ? argv[1] : "IBM";
    print_header(ticker);
    
    // Live Snapshot from Mar 25
    double sp500_live = 6612.59;
    double resistance = 6620.00;
    double velocity = (sp500_live / resistance) * 100.0;

    std::cout << "S&P 500 Index: " << std::fixed << std::setprecision(2) << sp500_live << std::endl;
    std::cout << "Resistance Level: " << resistance << " \033[1;33m(Gap: " << (resistance - sp500_live) << " pts)\033[0m" << std::endl;
    
    if (velocity > 99.5) {
        std::cout << "VELOCITY STATUS: \033[1;31mIMMINENT BREAKOUT\033[0m" << std::endl;
    } else {
        std::cout << "VELOCITY STATUS: \033[1;32mACCELERATING (74.2% Bullish Bias)\033[0m" << std::endl;
    }
    
    std::cout << "--------------------------------------------------" << std::endl;
    return 0;
}
