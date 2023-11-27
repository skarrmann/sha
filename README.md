# Sha Keyboard

**IMPORTANT: THIS PROJECT IS WORK IN PROGRESS. I AM CURRENTLY VERIFYING THE PCB BEFORE PRINTING IT, BUT FEEL FREE TO LOOK AROUND!**

Sha is a 50 key ortholinear keyboard, powered by either a Waveshare RP2040-Zero or RP2040-Matrix.

## Project structure

* [`gerbers`](gerbers): Gerber files for PCB manufacturing
* [`graphics`](graphics): Source assets for PCB silkscreen
* [`kicad`](kicad): KiCad project files (schematics and PCB designs)
* [`kicad-libraries`](kicad-libraries): KiCad components and footprints
* [`images`](images): Images for project documentation
* [`firmware`](firmware): Firmware files

## PCB

The PCB is designed for MX switches.

The Waveshare RP2040-Zero/Matrix footprint uses surface-mount solder pads. The castellated pads of the MCU board are soldered directly onto the PCB.

Each build uses two copies of the main PCB. This PCB acts as both the logical PCB, and when flipped the long way, it acts as a bottom plate to be attached the logical PCB.

An optional top plate PCB is available in the gerber files. This top plate covers the diodes and the solder pads of the MCU board.

## Keyboard firmware

*TBD*

## Bill of materials

Part | Purpose | Quantity | Notes
---- | ------- | -------- | -----
Main PCB  | circuit board and bottom plate | 2 | Send Gerber zip files to [JLCPCB](https://jlcpcb.com/)
Top plate PCB | protects diodes and MCU board | 1 |
Waveshare RP2040-Zero | Microcontroller board | 1 | Also supports Waveshare RP2040-Matrix
Keyswitches |  | 50 | PCB mount (5 pin) switches recommended
Keycaps |  | 50
M2 6mm screws | Secure main PCB and bottom plate PCB | 8 |
M2 nuts | 8 to secure main PCB and bottom plate PCB, 4 as spacers for top plate | 12 |
2mm tall rubber bumpons | Raise board above desk surface and provide skid resitance | 8 | 

## PCB manufacturing settings

These are the manufacturing settings I used when ordering from JLCPCB:

* **Base Material**: FR4
* **Layers**: 2
* **Dimensions**: (whatever the gerber file specifies)
* **PCB Qty**: 5
* **Different Design**: 1
* **Delivery Format**: Single PCB
* **PCB Thickness**: 1.6
* **PCB Color**: Black
* **Silkscreen**: White
* **Surface Finish**: LeadFree HASL-RoHS
* **Outer Copper Weight**: 1 oz
* **Gold Fingers**: No
* **Confirm Production File**: No
* **Flying Probe Test**: Fully Test
* **Castellated Holes**: No
* **Remove Order Number**: Specify a location

**IMPORTANT:** The PCB has ["JLCJLCJLCJLC" silkscreen text](https://support.jlcpcb.com/article/28-how-to-remove-order-number-from-your-pcb) on top side of the board. If you want to remove the order number from the boards or you want to print the PCBs with another manufacturer, then I recommend removing this silkscreen text from the `.kicad_pcb` file, and then regenerate the Gerber files.

## Build tips

## KiCad project notes

## Revision history

* **Sha 1.0** (2023-11-26)
     * Initial PCB design