#include"function_3.h"
#include "Header_Inside2_1.h"

int value_function_3_1=HEADER_MACRO_INSIDE2_1_VALUE_0,value_function_3_2=HEADER_MACRO_INSIDE2_1_VALUE_0,value_function_3_3=HEADER_MACRO_INSIDE2_1_VALUE_0;

int function_3_func1(int value1,int value2)
{
    static int return_value=0;
    if (value1 > value2)
    {
        return_value=value1-value2;
    }else
    {
        return_value=value2-value1;
    }

    return return_value;
}


int function_3_func2(int value1,int value2)
{
    static int return_value=0;
    if (value2 != 0) 
    {
        return_value=value1/value2;
    }else if(value1 !=0)
    {
        return_value=value2/value1;
    }

    return return_value;
}

int function_3_call(enum_function3 mode)
{
    static int return_value=0;
    switch (mode)
    {
    case enum_3_1:
        return_value=function_3_func1(value_function_3_1,value_function_3_2);
        break;
    case enum_3_2:
        return_value=function_3_func2(value_function_3_1,value_function_3_3);
        break;

    default:
        value_function_3_1=0;
        value_function_3_2=0;
        value_function_3_3=0;
        return_value=0;
        break;
    }
    return return_value;
}


int calculate(int value1,int value2)
{
    static int return_value=0;
    return_value=value1+value2;
    return return_value;
}


/**
  ******************************************************************************
  * @file    stm32f1xx_hal_adc.c
  * @author  MCD Application Team
  * @brief   This file provides firmware functions to manage the following 
  *          functionalities of the Analog to Digital Convertor (ADC)
  *          peripheral:
  *           + Initialization and de-initialization functions
  *           + Peripheral Control functions
  *           + Peripheral State functions
  *          Other functions (extended functions) are available in file 
  *          "stm32f1xx_hal_adc_ex.c".
  *
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2016 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  @verbatim
  ==============================================================================
                     ##### ADC peripheral features #####
  ==============================================================================
  [..]
  (+) 12-bit resolution

  (+) Interrupt generation at the end of regular conversion, end of injected
      conversion, and in case of analog watchdog or overrun events.
  
  (+) Single and continuous conversion modes.
  
  (+) Scan mode for conversion of several channels sequentially.
  
  (+) Data alignment with in-built data coherency.
  
  (+) Programmable sampling time (channel wise)
  
  (+) ADC conversion of regular group and injected group.

  (+) External trigger (timer or EXTI) 
      for both regular and injected groups.

  (+) DMA request generation for transfer of conversions data of regular group.

  (+) Multimode Dual mode (available on devices with 2 ADCs or more).
  
  (+) Configurable DMA data storage in Multimode Dual mode (available on devices
      with 2 DCs or more).
  
  (+) Configurable delay between conversions in Dual interleaved mode (available 
      on devices with 2 DCs or more).
  
  (+) ADC calibration

  (+) ADC supply requirements: 2.4 V to 3.6 V at full speed and down to 1.8 V at 
      slower speed.
  
  (+) ADC input range: from Vref- (connected to Vssa) to Vref+ (connected to 
      Vdda or to an external voltage reference).


                     ##### How to use this driver #####
  ==============================================================================
    [..]

     *** Configuration of top level parameters related to ADC ***
     ============================================================
     [..]

    (#) Enable the ADC interface
      (++) As prerequisite, ADC clock must be configured at RCC top level.
           Caution: On STM32F1, ADC clock frequency max is 14MHz (refer
                    to device datasheet).
                    Therefore, ADC clock prescaler must be configured in 
                    function of ADC clock source frequency to remain below
                    this maximum frequency.
        (++) One clock setting is mandatory:
             ADC clock (core clock, also possibly conversion clock).
             (+++) Example:
                   Into HAL_ADC_MspInit() (recommended code location) or with
                   other device clock parameters configuration:
               (+++) RCC_PeriphCLKInitTypeDef  PeriphClkInit;
               (+++) __ADC1_CLK_ENABLE();
               (+++) PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_ADC;
               (+++) PeriphClkInit.AdcClockSelection = RCC_ADCPCLK2_DIV2;
               (+++) HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit);

    (#) ADC pins configuration
         (++) Enable the clock for the ADC GPIOs
              using macro __HAL_RCC_GPIOx_CLK_ENABLE()
         (++) Configure these ADC pins in analog mode
              using function HAL_GPIO_Init()

    (#) Optionally, in case of usage of ADC with interruptions:
         (++) Configure the NVIC for ADC
              using function HAL_NVIC_EnableIRQ(ADCx_IRQn)
         (++) Insert the ADC interruption handler function HAL_ADC_IRQHandler() 
              into the function of corresponding ADC interruption vector 
              ADCx_IRQHandler().

    (#) Optionally, in case of usage of DMA:
         (++) Configure the DMA (DMA channel, mode normal or circular, ...)
              using function HAL_DMA_Init().
         (++) Configure the NVIC for DMA
              using function HAL_NVIC_EnableIRQ(DMAx_Channelx_IRQn)
         (++) Insert the ADC interruption handler function HAL_ADC_IRQHandler() 
              into the function of corresponding DMA interruption vector 
              DMAx_Channelx_IRQHandler().

     *** Configuration of ADC, groups regular/injected, channels parameters ***
     ==========================================================================
     [..]

    (#) Configure the ADC parameters (resolution, data alignment, ...)
        and regular group parameters (conversion trigger, sequencer, ...)
        using function HAL_ADC_Init().

    (#) Configure the channels for regular group parameters (channel number, 
        channel rank into sequencer, ..., into regular group)
        using function HAL_ADC_ConfigChannel().

    (#) Optionally, configure the injected group parameters (conversion trigger, 
        sequencer, ..., of injected group)
        and the channels for injected group parameters (channel number, 
        channel rank into sequencer, ..., into injected group)
        using function HAL_ADCEx_InjectedConfigChannel().

    (#) Optionally, configure the analog watchdog parameters (channels
        monitored, thresholds, ...)
        using function HAL_ADC_AnalogWDGConfig().

    (#) Optionally, for devices with several ADC instances: configure the 
        multimode parameters
        using function HAL_ADCEx_MultiModeConfigChannel().

     *** Execution of ADC conversions ***
     ====================================
     [..]

    (#) Optionally, perform an automatic ADC calibration to improve the
        conversion accuracy
        using function HAL_ADCEx_Calibration_Start().

    (#) ADC driver can be used among three modes: polling, interruption,
        transfer by DMA.

        (++) ADC conversion by polling:
          (+++) Activate the ADC peripheral and start conversions
                using function HAL_ADC_Start()
          (+++) Wait for ADC conversion completion 
                using function HAL_ADC_PollForConversion()
                (or for injected group: HAL_ADCEx_InjectedPollForConversion() )
          (+++) Retrieve conversion results 
                using function HAL_ADC_GetValue()
                (or for injected group: HAL_ADCEx_InjectedGetValue() )
          (+++) Stop conversion and disable the ADC peripheral 
                using function HAL_ADC_Stop()

        (++) ADC conversion by interruption: 
          (+++) Activate the ADC peripheral and start conversions
                using function HAL_ADC_Start_IT()
          (+++) Wait for ADC conversion completion by call of function
                HAL_ADC_ConvCpltCallback()
                (this function must be implemented in user program)
                (or for injected group: HAL_ADCEx_InjectedConvCpltCallback() )
          (+++) Retrieve conversion results 
                using function HAL_ADC_GetValue()
                (or for injected group: HAL_ADCEx_InjectedGetValue() )
          (+++) Stop conversion and disable the ADC peripheral 
                using function HAL_ADC_Stop_IT()

        (++) ADC conversion with transfer by DMA:
          (+++) Activate the ADC peripheral and start conversions
                using function HAL_ADC_Start_DMA()
          (+++) Wait for ADC conversion completion by call of function
                HAL_ADC_ConvCpltCallback() or HAL_ADC_ConvHalfCpltCallback()
                (these functions must be implemented in user program)
          (+++) Conversion results are automatically transferred by DMA into
                destination variable address.
          (+++) Stop conversion and disable the ADC peripheral 
                using function HAL_ADC_Stop_DMA()

        (++) For devices with several ADCs: ADC multimode conversion 
             with transfer by DMA:
          (+++) Activate the ADC peripheral (slave) and start conversions
                using function HAL_ADC_Start()
          (+++) Activate the ADC peripheral (master) and start conversions
                using function HAL_ADCEx_MultiModeStart_DMA()
          (+++) Wait for ADC conversion completion by call of function
                HAL_ADC_ConvCpltCallback() or HAL_ADC_ConvHalfCpltCallback()
                (these functions must be implemented in user program)
          (+++) Conversion results are automatically transferred by DMA into
                destination variable address.
          (+++) Stop conversion and disable the ADC peripheral (master)
                using function HAL_ADCEx_MultiModeStop_DMA()
          (+++) Stop conversion and disable the ADC peripheral (slave)
                using function HAL_ADC_Stop_IT()

     [..]

    (@) Callback functions must be implemented in user program:
      (+@) HAL_ADC_ErrorCallback()
      (+@) HAL_ADC_LevelOutOfWindowCallback() (callback of analog watchdog)
      (+@) HAL_ADC_ConvCpltCallback()
      (+@) HAL_ADC_ConvHalfCpltCallback
      (+@) HAL_ADCEx_InjectedConvCpltCallback()

     *** Deinitialization of ADC ***
     ============================================================
     [..]

    (#) Disable the ADC interface
      (++) ADC clock can be hard reset and disabled at RCC top level.
        (++) Hard reset of ADC peripherals
             using macro __ADCx_FORCE_RESET(), __ADCx_RELEASE_RESET().
        (++) ADC clock disable
             using the equivalent macro/functions as configuration step.
             (+++) Example:
                   Into HAL_ADC_MspDeInit() (recommended code location) or with
                   other device clock parameters configuration:
               (+++) PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_ADC
               (+++) PeriphClkInit.AdcClockSelection = RCC_ADCPLLCLK2_OFF
               (+++) HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit)

    (#) ADC pins configuration
         (++) Disable the clock for the ADC GPIOs
              using macro __HAL_RCC_GPIOx_CLK_DISABLE()

    (#) Optionally, in case of usage of ADC with interruptions:
         (++) Disable the NVIC for ADC
              using function HAL_NVIC_EnableIRQ(ADCx_IRQn)

    (#) Optionally, in case of usage of DMA:
         (++) Deinitialize the DMA
              using function HAL_DMA_Init().
         (++) Disable the NVIC for DMA
              using function HAL_NVIC_EnableIRQ(DMAx_Channelx_IRQn)

    [..]
    
    *** Callback registration ***
    =============================================
    [..]

     The compilation flag USE_HAL_ADC_REGISTER_CALLBACKS, when set to 1,
     allows the user to configure dynamically the driver callbacks.
     Use Functions HAL_ADC_RegisterCallback()
     to register an interrupt callback.
    [..]

     Function HAL_ADC_RegisterCallback() allows to register following callbacks:
       (+) ConvCpltCallback               : ADC conversion complete callback
       (+) ConvHalfCpltCallback           : ADC conversion DMA half-transfer callback
       (+) LevelOutOfWindowCallback       : ADC analog watchdog 1 callback
       (+) ErrorCallback                  : ADC error callback
       (+) InjectedConvCpltCallback       : ADC group injected conversion complete callback
       (+) MspInitCallback                : ADC Msp Init callback
       (+) MspDeInitCallback              : ADC Msp DeInit callback
     This function takes as parameters the HAL peripheral handle, the Callback ID
     and a pointer to the user callback function.
    [..]

     Use function HAL_ADC_UnRegisterCallback to reset a callback to the default
     weak function.
    [..]

     HAL_ADC_UnRegisterCallback takes as parameters the HAL peripheral handle,
     and the Callback ID.
     This function allows to reset following callbacks:
       (+) ConvCpltCallback               : ADC conversion complete callback
       (+) ConvHalfCpltCallback           : ADC conversion DMA half-transfer callback
       (+) LevelOutOfWindowCallback       : ADC analog watchdog 1 callback
       (+) ErrorCallback                  : ADC error callback
       (+) InjectedConvCpltCallback       : ADC group injected conversion complete callback
       (+) MspInitCallback                : ADC Msp Init callback
       (+) MspDeInitCallback              : ADC Msp DeInit callback
     [..]

     By default, after the HAL_ADC_Init() and when the state is HAL_ADC_STATE_RESET
     all callbacks are set to the corresponding weak functions:
     examples HAL_ADC_ConvCpltCallback(), HAL_ADC_ErrorCallback().
     Exception done for MspInit and MspDeInit functions that are
     reset to the legacy weak functions in the HAL_ADC_Init()/ HAL_ADC_DeInit() only when
     these callbacks are null (not registered beforehand).
    [..]

     If MspInit or MspDeInit are not null, the HAL_ADC_Init()/ HAL_ADC_DeInit()
     keep and use the user MspInit/MspDeInit callbacks (registered beforehand) whatever the state.
     [..]

     Callbacks can be registered/unregistered in HAL_ADC_STATE_READY state only.
     Exception done MspInit/MspDeInit functions that can be registered/unregistered
     in HAL_ADC_STATE_READY or HAL_ADC_STATE_RESET state,
     thus registered (user) MspInit/DeInit callbacks can be used during the Init/DeInit.
    [..]

     Then, the user first registers the MspInit/MspDeInit user callbacks
     using HAL_ADC_RegisterCallback() before calling HAL_ADC_DeInit()
     or HAL_ADC_Init() function.
     [..]
/* /*   /*
static int  slider_set_callback(void *cb)
{




}
     When the compilation flag USE_HAL_ADC_REGISTER_CALLBACKS is set to 0 or
     not defined, the callback registration feature is not available and all callbacks
     are set to the corresponding weak functions.
  
  @endverbatim
  */
//*/
/******;{  //{}; dfgdf  ; */ ;  static int  slider_set_callback(void *cb)  ;/*/// static int  slider_set_callback(void *cb)  ; ////////////////*/

  static int  slider_set_callback(void *cb)  /*/// static int  slider_set_callback(void *cb)  ; ////////////////*/
  {}
/*
*/  /*****//*;{  //{}; dfgdf  ; */ /******;{  //{}; dfgdf  ;/* */  static int  slider_set_callback(void *cb)  /*/// static int  slider_set_callback(void *cb)  ; ////////////////*/

/* /* */  /*
static int  slider_set_callback(void *cb)
{




}
     When the compilation flag USE_HAL_ADC_REGISTER_CALLBACKS is set to 0 or
     not defined, the callback registration feature is not available and all callbacks
     are set to the corresponding weak functions.
  
  @endverbatim
  */
//*/

{}