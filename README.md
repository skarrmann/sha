# Sha Keyboard

## Project structure

* [`gerbers`](gerbers): Gerber files for PCB manufacturing
* [`graphics`](graphics): Source assets for PCB silkscreen
* [`kicad`](kicad): KiCad project files (schematics and PCB designs)
* [`kicad-libraries`](kicad-libraries): KiCad components and footprints
* [`images`](images): Images for project documentation
* [`firmware`](firmware): Firmware files

## PCB

## Keyboard firmware

## Bill of materials

Vendor URLs are just recommendations based on quality/affordablity. I have purchased from these vendors, but have no personal affiliation with them.

Part | Purpose | Quantity | Notes
---- | ------- | -------- | -----
PCB  | circuit board and bottom plate | 2 | | Send Gerber zip files to [JLCPCB](https://jlcpcb.com/).
Waveshare RP2040-Matrix | Microcontroller board | 1 | Also supports Waveshare RP2040-Zero
Keyswitches |  | 50 | 
Keycaps |  | 50
M2 6mm screws | Secure main PCB and bottom plate PCB | 7 |
M2 nuts | Secure main PCB and bottom plate PCB | 7 |
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
* **PCB Color**: Blue
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