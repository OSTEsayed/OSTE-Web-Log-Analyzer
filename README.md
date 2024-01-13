# OSTE-Web-Log-Analyzer
![Project Logo](Lib/images/ostewla.png)

Automate the process of analyzing web server logs with the Python Web Log Analyzer. This powerful tool is designed to enhance security by identifying and detecting various types of cyber attacks within your server logs. Stay ahead of potential threats with features that include:


## Table of Contents

- [Features](#features)
- [Future Features](#Future Features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Features
1. Attack Detection: Identify and flag potential Cross-Site Scripting (XSS), Local File Inclusion (LFI), Remote File Inclusion (RFI), and other common web application attacks.

2. Rate Limit Monitoring: Detect suspicious patterns in multiple requests made in a short time frame, helping to identify brute-force attacks or automated scanning tools.

3. Automated Scanner Detection: Keep your web applications secure by identifying requests associated with known automated scanning tools or vulnerability scanners.

4. User-Agent Analysis: Analyze and identify potentially malicious User-Agent strings, allowing you to spot unusual or suspicious behavior.

## Future Features

This project is actively developed, and future features may include:

1. IP Geolocation: Identify the geographic location of IP addresses in the logs.
2. Real-time Monitoring: Implement real-time monitoring capabilities for immediate threat detection.

## Installation

The tool only requires Python 3 at the moment.

1. step1: 
    git clone https://github.com/OSTEsayed/OSTE-Web-Log-Analyzer.git
2. step2:
    cd OSTE-Web-Log-Analyzer
3. step3:
    python3 WLA-cli.py

## Usage

After cloning the repository to your local machine, you can initiate the application by executing the command python3 WLA-cli.py. 
simple usage example : python3 WLA-cli.py -l LogSampls/access.log -t

use -h or --help for more detailed usage examples : python3 WLA-cli.py -h

## Contributing

We welcome contributions to enhance and improve this project. 
either by donation :  
  [![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/oudjanisaye)
 
or by your power of mind .contribute, please follow these guidelines:

   1. Fork the repository and create a new branch for your contribution.
   2. Ensure that your code adheres to the project's coding standards.
   3. Make your changes, addressing the specific issue or adding the proposed enhancement.
   4. Test your changes thoroughly.
   5. Commit your changes and provide a clear and descriptive commit message.
   6. Push your changes to your forked repository.
   7. Submit a pull request, detailing the changes you've made and providing any relevant information or context.

Please note that all contributions will be reviewed by the project maintainers. We appreciate your effort and will do our best to provide timely feedback.

If you have any questions or need further clarification, feel free to reach out to us through the issue tracker or by contacting the project maintainers directly.

## License

This project is under  GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.

This project is intended for educational purposes and aims to simplify the overall assessment of cybersecurity. However, we want to emphasize that we are not liable for any malicious use of this application. It is crucial that users of this software exercise responsibility and ethical behavior. We strongly recommend notifying the targets or individuals involved before utilizing this software.

## Contact
   linkdin:(https://www.linkedin.com/in/oudjani-seyyid-taqy-eddine-b964a5228)


