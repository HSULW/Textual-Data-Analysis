#ifndef FIREWALL_H
#define FIREWALL_H

#include <stdint.h>

// 函數指針，用於表示規則函數
int32_t (*rule)(const uint8_t *p_input_packet, const int32_t input_size,
                uint8_t **pp_output_packet, int32_t *p_output_size);

// 設置第idx條規則的函數指針
int32_t set_rule(int32_t idx, int32_t (*rule)(const uint8_t *, const int32_t,
                                              uint8_t **, int32_t *));

// 取消設置第idx條規則的函數指針
int32_t unset_rule(int32_t idx);

// 對輸入封包應用所有規則，並存儲每個輸出封包
int32_t filter(const uint8_t *p_input_packets, const int32_t input_size,
               uint8_t **pp_output_packets, int32_t *p_output_size);

#endif // FIREWALL_H
