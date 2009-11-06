
; *** Fade screen & object (sprite) palettes to white ***
; v1.0 - initial version

FADE_TO_WHITE   equ 1           ; Set this to 0 to fade to black


lcd_FadeOut::

        ld      b,32
.loop0:
        push    bc

; Wait for next screen redraw
.skip:
        ld      a,[rLY]
        or      a
        jr      nz,.skip

        ld      b,$80
.loop1:
        ld      c,$69

; Read BG color register pair

        ld      a,b
        ld      [rBCPS],a

        di
        lcd_WaitVRAM

        ld      a,[c]
        ld      e,a

        ld      a,b
        inc     a
        ld      [rBCPS],a

        ld      a,[c]
        ei

        ld      d,a

; Fade color register pair to white

        call    ConvertColor15to24
 if FADE_TO_WHITE
        call    MakeLighter
 else
        call    MakeDarker
 endc
        call    ConvertColor24to15

; Write BG color register pair

        ld      a,b
        ld      [rBCPS],a

        di
        lcd_WaitVRAM

        ld      a,e
        ld      [c],a

        ld      a,d
        ld      [c],a

        ei

        ld      c,$6b

; Read OBJ color register pair

        ld      a,b
        ld      [rOCPS],a

        di
        lcd_WaitVRAM

        ld      a,[c]
        ld      e,a

        ld      a,b
        inc     a
        ld      [rOCPS],a

        ld      a,[c]
        ei

        ld      d,a

; Fade color register pair to white

        call    ConvertColor15to24
 if FADE_TO_WHITE
        call    MakeLighter
 else
        call    MakeDarker
 endc
        call    ConvertColor24to15

; Write OBJ color register pair

        ld      a,b
        ld      [rOCPS],a

        di
        lcd_WaitVRAM

        ld      a,e
        ld      [c],a

        ld      a,d
        ld      [c],a

        ei

        inc     b
        inc     b

        ld      a,$80+$40 ;-16
        cp      b               ; Are we done?
        jr      nz,.loop1       ; not yet

        pop     bc
        dec     b               ; Are we done yet?
        jp      nz,.loop0       ; not yet

        ret

; Entry:
;   D = high byte, E = low byte
; Exit:
;   H = Blue, L = Green, A = Red

ConvertColor15to24:
        ld      a,e

        srl     d
        rr      e
        srl     d
        rr      e
        ld      h,d

        srl     e
        srl     e
        srl     e
        ld      l,e

        and     $1f
        ret

; Entry:
;   H = Blue, L = Green, A = Red
; Exit:
;   D = high byte, E = low byte

ConvertColor24to15:
        rlca
        rlca
        rlca
        ld      e,a
        srl     l
        rr      e
        srl     l
        rr      e
        srl     l
        rr      e

        ld      a,h
        add     a
        add     a
        add     l
        ld      d,a

        ret

FadeIn:
        ret

MakeLighter:
        cp      31
        adc     0
        ld      d,a

        ld      a,l
        cp      31
        adc     0
        ld      l,a

        ld      a,h
        cp      31
        adc     0
        ld      h,a

        ld      a,d
        ret

MakeDarker:
        or      a
        jr      z,.skip1
        dec     a
.skip1:
        ld      d,a

        xor     a
        cp      l
        jr      z,.skip2
        dec     l
.skip2:

        cp      h
        jr      z,.skip3
        dec     h
.skip3:

        ld      a,d
        ret
