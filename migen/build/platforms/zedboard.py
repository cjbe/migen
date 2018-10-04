from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform


# Bank 34 and 35 voltage depend on J18 jumper setting
_io = [
        ("clk100", 0, Pins("Y9"), IOStandard("LVCMOS33")),

        ("user_btn", 0, Pins("P16"), IOStandard("LVCMOS25")),  # center
        ("user_btn", 1, Pins("R16"), IOStandard("LVCMOS25")),  # down
        ("user_btn", 2, Pins("N15"), IOStandard("LVCMOS25")),  # left
        ("user_btn", 3, Pins("R18"), IOStandard("LVCMOS25")),  # right
        ("user_btn", 4, Pins("T18"), IOStandard("LVCMOS25")),  # up

        ("user_sw", 0, Pins("F22"), IOStandard("LVCMOS25")),
        ("user_sw", 1, Pins("G22"), IOStandard("LVCMOS25")),
        ("user_sw", 2, Pins("H22"), IOStandard("LVCMOS25")),
        ("user_sw", 3, Pins("F21"), IOStandard("LVCMOS25")),
        ("user_sw", 4, Pins("H19"), IOStandard("LVCMOS25")),
        ("user_sw", 5, Pins("H18"), IOStandard("LVCMOS25")),
        ("user_sw", 6, Pins("H17"), IOStandard("LVCMOS25")),
        ("user_sw", 7, Pins("M15"), IOStandard("LVCMOS25")),

        ("user_led", 0, Pins("T22"), IOStandard("LVCMOS33")),
        ("user_led", 1, Pins("T21"), IOStandard("LVCMOS33")),
        ("user_led", 2, Pins("U22"), IOStandard("LVCMOS33")),
        ("user_led", 3, Pins("U21"), IOStandard("LVCMOS33")),
        ("user_led", 4, Pins("V22"), IOStandard("LVCMOS33")),
        ("user_led", 5, Pins("W22"), IOStandard("LVCMOS33")),
        ("user_led", 6, Pins("U19"), IOStandard("LVCMOS33")),
        ("user_led", 7, Pins("U14"), IOStandard("LVCMOS33")),

        # A
        ("pmod", 0, Pins("Y11 AA11 Y10 AA9 AB11 AB10 AB9 AA8"),
            IOStandard("LVCMOS33")),
        # B
        ("pmod", 1, Pins("W12 W11 V10 W8 V12 W10 V9 V8"),
            IOStandard("LVCMOS33")),
        # C
        ("pmod", 2,
            Subsignal("n", Pins("AB6 AA4 T6 U4")),
            Subsignal("p", Pins("AB7 Y4 R6 T4")),
            IOStandard("LVCMOS33")),
        # D
        ("pmod", 3,
            Subsignal("n", Pins("W7 V4 W5 U5")),
            Subsignal("p", Pins("V7 V5 W6 U6")),
            IOStandard("LVCMOS33")),

        ("audio", 0,
            Subsignal("adr", Pins("AB1 Y5")),
            Subsignal("gpio", Pins("Y8 AA7 AA6 Y6")),
            Subsignal("mclk", Pins("AB2")),
            Subsignal("sck", Pins("AB4")),
            Subsignal("sda", Pins("AB5")),
            IOStandard("LVCMOS33")),

        ("oled", 0,
            Subsignal("dc", Pins("U10")),
            Subsignal("res", Pins("U9")),
            Subsignal("sclk", Pins("AB12")),
            Subsignal("sdin", Pins("AA12")),
            Subsignal("vbat", Pins("U11")),
            Subsignal("vdd", Pins("U12")),
            IOStandard("LVCMOS33")),

        ("hdmi", 0,
            Subsignal("clk", Pins("W18")),
            Subsignal("d", Pins(
                "Y13 AA13 AA14 Y14 AB15 AB16 AA16 AB17 "
                "AA17 Y15 W13 W15 V15 U17 V14 V13")),
            Subsignal("de", Pins("U16")),
            Subsignal("hsync", Pins("V17")),
            Subsignal("vsync", Pins("W17")),
            Subsignal("int", Pins("W16")),
            Subsignal("scl", Pins("AA18")),
            Subsignal("sda", Pins("Y16")),
            Subsignal("spdif", Pins("U15")),
            Subsignal("spdifo", Pins("Y18")),
            IOStandard("LVCMOS33")),

        ("netic16", 0,
            Subsignal("w20", Pins("W20")),
            Subsignal("w21", Pins("W21")),
            IOStandard("LVCMOS33")),

        ("vga", 0,
            Subsignal("r", Pins("V20 U20 V19 V18")),
            Subsignal("g", Pins("AB22 AA22 AB21 AA21")),
            Subsignal("b", Pins("Y21 Y20 AB20 AB19")),
            Subsignal("hsync_n", Pins("AA19")),
            Subsignal("vsync_n", Pins("Y19")),
            IOStandard("LVCMOS33")),

        ("usb_otg", 0,
            Subsignal("vbusoc", Pins("L16")),
            Subsignal("reset_n", Pins("G17")),
            IOStandard("LVCMOS18")),

        ("pudc_b", 0, Pins("K16"), IOStandard("LVCMOS18")),

        ("xadc", 0,
            Subsignal("gio", Pins("H15 R15 K15 J15")),
            Subsignal("ad0_n", Pins("E16")),
            Subsignal("ad0_p", Pins("F16")),
            Subsignal("ad8_n", Pins("D17")),
            Subsignal("ad8_p", Pins("D16")),
            IOStandard("LVCMOS18")),
]


_connectors = [
    ("fmc", {
        "LA33_N": "B22",
        "LA32_N": "A22",
        "LA31_N": "B17",
        "LA30_N": "B15",
        "LA29_N": "C18",
        "LA28_N": "A17",
        "LA27_N": "D21",
        "LA26_N": "E18",
        "LA25_N": "C22",
        "LA24_N": "A19",
        "LA23_N": "D15",
        "LA22_N": "F19",
        "LA21_N": "E20",
        "LA20_N": "G21",
        "LA19_N": "G16",
        "LA18_CC_N": "C20",
        "LA17_CC_N": "B20",
        "LA16_N": "K21",
        "LA15_N": "J17",
        "LA14_N": "K20",
        "LA13_N": "M17",
        "LA12_N": "P21",
        "LA11_N": "N18",
        "LA10_N": "T19",
        "LA09_N": "R21",
        "LA08_N": "J22",
        "LA07_N": "T17",
        "LA06_N": "L22",
        "LA05_N": "K18",
        "LA04_N": "M22",
        "LA03_N": "P22",
        "LA02_N": "P18",
        "LA01_CC_N": "N20",
        "LA00_CC_N": "M20",
        "LA33_P": "B21",
        "LA32_P": "A21",
        "LA31_P": "B16",
        "LA30_P": "C15",
        "LA29_P": "C17",
        "LA28_P": "A16",
        "LA27_P": "E21",
        "LA26_P": "F18",
        "LA25_P": "D22",
        "LA24_P": "A18",
        "LA23_P": "E15",
        "LA22_P": "G19",
        "LA21_P": "E19",
        "LA20_P": "G20",
        "LA19_P": "G15",
        "LA18_CC_P": "D20",
        "LA17_CC_P": "B19",
        "LA16_P": "J20",
        "LA15_P": "J16",
        "LA14_P": "K19",
        "LA13_P": "L17",
        "LA12_P": "P20",
        "LA11_P": "N17",
        "LA10_P": "R19",
        "LA09_P": "R20",
        "LA08_P": "J21",
        "LA07_P": "T16",
        "LA06_P": "L21",
        "LA05_P": "J18",
        "LA04_P": "M21",
        "LA03_P": "N22",
        "LA02_P": "P17",
        "LA01_CC_P": "N19",
        "LA00_CC_P": "M19",
        # LVDS
        "CLK0_M2C_N": "L19",
        "CLK0_M2C_P": "L18",
        "CLK1_M2C_N": "C19",
        "CLK1_M2C_P": "D18",
        # DIFF_HSTL_I_DCI_18
        "GBTCLK0_M2C_P": "",
        "GBTCLK0_M2C_N": "",
        "DP0_M2C_P": "",
        "DP0_M2C_N": "",
        "DP0_C2M_P": "",
        "DP0_C2M_N": "",
    }),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7z020-clg484-1", _io, _connectors,
                toolchain="vivado")
