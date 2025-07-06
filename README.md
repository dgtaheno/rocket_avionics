<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/dgtaheno/rocket_avionics">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Rocket Avionics Dashboard</h3>

  <p align="center">
    Real-time or post-flight telemetry dashboard to visualize altitude, GPS trajectory, and vertical acceleration for amateur or educational rocketry.
    <br />
    <a href="https://github.com/dgtaheno/rocket_avionics"><strong>Explore the project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dgtaheno/rocket_avionics">View Demo</a>
    ·
    <a href="https://github.com/dgtaheno/rocket_avionics/issues">Report Bug</a>
    ·
    <a href="https://github.com/dgtaheno/rocket_avionics/issues">Request Feature</a>
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a simple telemetry dashboard using Dash and Plotly in Python, designed to display flight data from a CSV file. It includes real-time updates and clear visualization for:

* GPS position on a map (latitude, longitude)
* Altitude over time
* Vertical acceleration (Z-axis)

It is ideal for educational rocket launches, post-flight analysis, or integration with telemetry loggers.

### Built With

* [Dash](https://dash.plotly.com/)
* [Plotly](https://plotly.com/python/)
* [Pandas](https://pandas.pydata.org/)
* [Python 3.7+](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>
<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

```bash
pip install dash pandas plotly
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/dgtaheno/rocket-telemetry-dashboard.git
cd rocket-telemetry-dashboard
```

2. Add or generate a telemetry data file named `data.csv` with the following format:

```csv
timestamp_ms,lat_deg,lon_deg,altitude_m,accZ_m_s2
0,53.68300,10.23900,0.0,0.0
1000,53.68302,10.23902,50.5,12.3
...
```

3. Run the dashboard:

```bash
python dashboard.py
```

Then open `http://127.0.0.1:8050/` in your browser.

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

The dashboard will refresh data every second using Dash's `dcc.Interval`. It can be used in:

* **Post-flight mode**: Load a static or updating CSV with telemetry logs.
* **Real-time mode** (future): Stream data from a microcontroller or telemetry module.

The map shows the GPS track, while plots for altitude and acceleration help analyze each flight phase.

<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

* [x] Real-time CSV parsing
* [x] Interactive map with GPS path
* [x] Altitude and acceleration plots
* [ ] Phase detection overlay (launch, apogee, descent, landing)
* [ ] Real-time serial/LoRa integration
* [ ] Export to report (PDF/CSV)

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

David García-Taheno Fernández – [dgtaheno@hotmail.com](mailto:dgtaheno@hotmail.com)
Project Link: [https://github.com/dgtaheno/rocket_avionics](https://github.com/dgtaheno/rocket_avionics)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

* [Dash Docs](https://dash.plotly.com/)
* [Plotly Python](https://plotly.com/python/)
* [CSV Rocket Telemetry Log Format](https://github.com/)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/dgtaheno/rocket_avionics.svg?style=for-the-badge
[contributors-url]: https://github.com/dgtaheno/rocket_avionics/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dgtaheno/rocket_avionics.svg?style=for-the-badge
[forks-url]: https://github.com/dgtaheno/rocket_avionics/network/members
[stars-shield]: https://img.shields.io/github/stars/dgtaheno/rocket_avionics.svg?style=for-the-badge
[stars-url]: https://github.com/dgtaheno/rocket_avionics/stargazers
[issues-shield]: https://img.shields.io/github/issues/dgtaheno/rocket_avionics.svg?style=for-the-badge
[issues-url]: https://github.com/dgtaheno/rocket_avionics/issues
[license-shield]: https://img.shields.io/github/license/dgtaheno/rocket_avionics.svg?style=for-the-badge
[license-url]: https://github.com/dgtaheno/rocket_avionics/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dgtaheno/
[product-screenshot]: logo.png
