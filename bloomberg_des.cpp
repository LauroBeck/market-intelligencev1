#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    std::string ticker = (argc > 1) ? argv[1] : "IBM";
    std::cout << "\033[1;37;44m " << ticker << " US Equity             Security Description (DES) \033[0m" << std::endl;
    std::cout << "NAME: INTERNATIONAL BUSINESS MACHINES CORP" << std::endl;
    std::cout << "SECTOR: TECHNOLOGY | INDUSTRY: IT SERVICES" << std::endl;
    std::cout << "MARKET CAP: ~180.5B | STATUS: ACTIVE AUDIT" << std::endl;
    std::cout << "--------------------------------------------------" << std::endl;
    return 0;
}
